from src.state import EditalState


def test_state_aceita_campos_minimos():
    """Garante que o schema aceita pelo menos o campo obrigatório.

    Testes de integração de verdade (rodando o grafo com um PDF real)
    entram quando os nós de leitura/conformidade estiverem implementados
    para valer — por ora isso só documenta o contrato do estado.
    """
    estado: EditalState = {
        "caminho_pdf": "data/editais/exemplo.pdf",
        "texto_bruto": None,
        "dados_extraidos": None,
        "status_conformidade": None,
        "pendencias": None,
    }

    assert estado["caminho_pdf"] == "data/editais/exemplo.pdf"
