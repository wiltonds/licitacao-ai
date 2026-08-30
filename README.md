# Assistente de Inteligência para Licitações Públicas

Projeto de estudo e portfólio: um sistema multiagente (LangGraph + Claude) que lê
editais de licitação pública brasileiros e cruza o conteúdo com a legislação
vigente — o primeiro passo de um pipeline maior de automação de licitações.

## Contexto

Empresas que dependem de licitação pública para operar (por exemplo,
terceirizadoras de serviços) enfrentam um gargalo real: cada edital tem
dezenas de páginas de exigências, e interpretar mal uma cláusula custa a
desclassificação. Este projeto ataca essa dor com um pipeline de agentes
especializados, cada um responsável por uma etapa do processo.

## Arquitetura (visão completa do sistema)

O sistema completo é dividido em cinco fases:

1. **Descoberta** — encontrar editais relevantes em múltiplos portais
   (fora do escopo deste repositório; hoje coberto por ferramentas de
   terceiros, como plataformas de monitoramento de licitações)
2. **Inteligência do edital** — leitura + cruzamento com a legislação
   (🚧 **fase atual deste repositório**)
3. **Preparação** — impugnação, planilha de proposta, cadastro
4. **Participação ativa** — chat com o pregoeiro, execução no portal
5. **Pós-sessão** — recursos, diligências, homologação

Este repositório implementa a **Fase 2** como MVP: um grafo de dois nós
(`leitura` → `conformidade`) construído com LangGraph.

## Estrutura

```
src/
  state.py              # schema do estado compartilhado entre os nós
  graph.py               # monta e compila o grafo (StateGraph)
  nodes/
    leitura.py            # nó 1: extrai texto do PDF do edital
    conformidade.py        # nó 2: checa conformidade com a legislação (stub)
  rag/                    # lógica de indexação/recuperação (a construir)
data/
  editais/                # PDFs de exemplo (não versionados)
  legislacao/             # textos de legislação para RAG (não versionados)
tests/
  test_state.py           # testes básicos
```

## Como rodar

1. Crie um ambiente virtual: `python -m venv .venv && source .venv/bin/activate`
2. Instale as dependências: `pip install -r requirements.txt`
3. Copie `.env.example` para `.env` e adicione sua `ANTHROPIC_API_KEY`
4. Coloque um edital de exemplo em `data/editais/exemplo.pdf`
5. Rode: `python -m src.graph`

## Roadmap

- [x] Estrutura do grafo (state + 2 nós stub)
- [x] Extração estruturada do edital via tool calling (Claude), com leitura direta de PDFs escaneados via visão
- [ ] Cruzamento real com a Lei 14.133/2021 via RAG
- [ ] Aresta condicional: gerar impugnação quando houver não conformidade
- [ ] Fases 3, 4 e 5

## Stack

Python · LangGraph · Claude (Anthropic API) · ChromaDB
