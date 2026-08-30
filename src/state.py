from typing import Optional, TypedDict


class EditalState(TypedDict):
    """Estado compartilhado entre os nós do grafo.

    Este é o "contrato" do pipeline: cada nó recebe uma cópia deste
    dicionário, lê os campos que precisa, e devolve APENAS os campos
    que ele atualiza. O LangGraph cuida de fazer o merge no estado
    global — nenhum nó precisa conhecer o que os outros fazem.

    Pense nisso como a mesa onde todos os agentes deixam e pegam
    informação, em vez de conversarem diretamente entre si.
    """

    # entrada: uma licitação real é um CONJUNTO de documentos (edital +
    # anexos + termo de referência), não um único PDF — descobrimos isso
    # na prática quando exigencias_habilitacao veio vazio de um edital
    # cujas exigências estavam num anexo separado.
    pasta_licitacao: str

    # preenchido pelo nó "leitura"
    texto_bruto: Optional[str]
    dados_extraidos: Optional[dict]

    # preenchido pelo nó "conformidade"
    status_conformidade: Optional[str]  # "apto" | "nao_apto" | "pendente"
    pendencias: Optional[list[str]]
