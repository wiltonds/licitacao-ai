import base64
from pathlib import Path

from anthropic import Anthropic
from pypdf import PdfReader

from src.nodes.schemas import DadosEdital
from src.state import EditalState

_CARACTERES_MINIMOS_POR_PAGINA = 50  # abaixo disso, tratamos como PDF escaneado

_PROMPT_SISTEMA = """Você extrai dados estruturados de editais de licitação
pública brasileiros a partir dos documentos fornecidos. Pode haver mais de
um documento (edital principal, anexos, termo de referência) — alguns
enviados como texto extraído, outros como o PDF em si (quando o texto não
pôde ser extraído por serem digitalizados/escaneados; nesse caso, leia o
conteúdo visualmente). Considere todos os documentos ao procurar cada
campo — exigências de habilitação, por exemplo, costumam estar em um
anexo separado do edital principal. Use a ferramenta extrair_dados_edital
para registrar o que encontrar."""

_TOOLS = [
    {
        "name": "extrair_dados_edital",
        "description": "Registra os dados estruturados extraídos do edital.",
        "input_schema": DadosEdital.model_json_schema(),
    }
]


def ler_edital(state: EditalState) -> dict:
    """Nó 1: lê todos os PDFs da pasta da licitação e pede ao Claude para
    estruturar os dados principais, considerando o conjunto de documentos.

    Lê: state["pasta_licitacao"]
    Escreve: state["texto_bruto"], state["dados_extraidos"]

       Cada PDF é tratado de um jeito: se o pypdf conseguiu extrair texto de
    verdade (edital principal, normalmente), mandamos o texto — mais
    barato. Se extraiu muito pouco (sinal de PDF escaneado, comum em
    Termo de Referência e Estudo Técnico Preliminar), mandamos o PDF
    inteiro para o Claude ler diretamente via visão, sem precisar de uma
    ferramenta de OCR separada.

    Achado de domínio: alguns editais dispensam a apresentação de
    documentos de habilitação já cadastrados no SICAF (Lei 14.133),
    então uma lista vazia em exigencias_habilitacao pode ser correta,
    não um erro de extração — vale revisitar isso quando integrarmos
    consulta ao SICAF de verdade.
    """
   

    pasta = Path(state["pasta_licitacao"])
    arquivos_pdf = sorted(pasta.glob("*.pdf"))

    if not arquivos_pdf:
        raise ValueError(f"Nenhum PDF encontrado em {pasta}")

    conteudo_mensagem = []
    texto_bruto_partes = []

    for caminho in arquivos_pdf:
        reader = PdfReader(str(caminho))
        texto_arquivo = "\n".join(page.extract_text() or "" for page in reader.pages)
        num_paginas = len(reader.pages) or 1

        if len(texto_arquivo) / num_paginas >= _CARACTERES_MINIMOS_POR_PAGINA:
            conteudo_mensagem.append({
                "type": "text",
                "text": f"=== documento: {caminho.name} (texto extraído) ===\n{texto_arquivo}",
            })
            texto_bruto_partes.append(f"=== documento: {caminho.name} ===\n{texto_arquivo}")
        else:
            dados_pdf = base64.standard_b64encode(caminho.read_bytes()).decode("utf-8")
            conteudo_mensagem.append({
                "type": "document",
                "source": {"type": "base64", "media_type": "application/pdf", "data": dados_pdf},
            })
            texto_bruto_partes.append(f"=== documento: {caminho.name} (escaneado, lido via visão) ===")

    client = Anthropic()
    resposta = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        system=_PROMPT_SISTEMA,
        tools=_TOOLS,
        tool_choice={"type": "tool", "name": "extrair_dados_edital"},
        messages=[{"role": "user", "content": conteudo_mensagem}],
    )

    bloco_tool = next(b for b in resposta.content if b.type == "tool_use")
    dados = DadosEdital(**bloco_tool.input)

    return {
        "texto_bruto": "\n\n".join(texto_bruto_partes),
        "dados_extraidos": dados.model_dump(),
    }