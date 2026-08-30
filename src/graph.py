from dotenv import load_dotenv

load_dotenv()
from langgraph.graph import END, StateGraph
from src.nodes.conformidade import checar_conformidade
from src.nodes.leitura import ler_edital
from src.state import EditalState


def construir_grafo():
    """Monta o grafo: dois nós, uma aresta linear entre eles.

    StateGraph(EditalState) diz ao LangGraph qual é o "formato" do
    estado que vai circular. add_node registra cada função como um
    passo do grafo. add_edge diz o que vem depois do quê. Isso é
    literalmente a estrutura toda — o resto é o conteúdo de cada nó.
    """
    grafo = StateGraph(EditalState)

    grafo.add_node("leitura", ler_edital)
    grafo.add_node("conformidade", checar_conformidade)

    grafo.set_entry_point("leitura")
    grafo.add_edge("leitura", "conformidade")
    grafo.add_edge("conformidade", END)

    return grafo.compile()


if __name__ == "__main__":
    import json

    app = construir_grafo()
    resultado = app.invoke({"pasta_licitacao": "data/editais/bento_goncalves_133_2026"})

    print("Tamanho do texto bruto:", len(resultado["texto_bruto"]), "caracteres")
    print()
    print("Dados extraidos:")
    print(json.dumps(resultado["dados_extraidos"], ensure_ascii=False, indent=2))
    print()
    print("Status conformidade (ainda placeholder):", resultado["status_conformidade"])