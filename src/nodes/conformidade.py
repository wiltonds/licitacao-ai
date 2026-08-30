from src.state import EditalState


def checar_conformidade(state: EditalState) -> dict:
    """Nó 2 (stub): vai cruzar `dados_extraidos` com a Lei 14.133/2021
    via RAG. Por enquanto só sinaliza que o nó rodou, para validarmos
    o grafo inteiro antes de implementar a lógica real.

    Próximo passo (quando formos construir isso de verdade):
    1. Indexar o texto da legislação em data/legislacao/ (chunking + embeddings)
    2. Buscar os trechos relevantes para cada exigência do edital
    3. Pedir ao Claude para comparar e apontar não conformidades
    """
    # TODO: substituir pelo cruzamento real com a legislação
    return {
        "status_conformidade": "pendente",
        "pendencias": ["conformidade ainda não implementada"],
    }
