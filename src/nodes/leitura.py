from pypdf import PdfReader

from src.state import EditalState


def ler_edital(state: EditalState) -> dict:
    """Nó 1: extrai o texto bruto do PDF do edital.

    Por enquanto só faz a extração de texto puro — a parte "inteligente"
    (pedir ao Claude para transformar esse texto em dados estruturados:
    objeto da licitação, prazos, exigências de habilitação) é o próximo
    passo, depois que o esqueleto do grafo estiver rodando ponta a ponta.

    Todo nó do LangGraph segue essa mesma forma: recebe o estado inteiro,
    devolve só o que mudou.
    """
    reader = PdfReader(state["caminho_pdf"])
    texto = "\n".join(page.extract_text() or "" for page in reader.pages)

    return {"texto_bruto": texto}
