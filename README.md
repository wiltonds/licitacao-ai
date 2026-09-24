# Public Procurement AI — Tender Intelligence with LangGraph

> Applied AI system that reads Brazilian public procurement documents, extracts structured requirements and prepares evidence-based compliance analysis through an agentic workflow.

**Portfolio focus:** Agentic AI · LangGraph · RAG · Document Intelligence · LLMs · Information Retrieval · Decision Support

![Architecture](./docs/architecture.svg)

## Business Problem

Public procurement documents can contain dozens or hundreds of pages of requirements, deadlines, qualifications, technical specifications and legal conditions.

For a company evaluating whether to participate, the first challenge is not simply generating text. It is **finding the relevant evidence, structuring the requirements and checking them consistently.**

This project explores an AI-assisted workflow for that problem.

## Solution

The current repository implements **Phase 2 — Tender Intelligence** of a larger procurement workflow:

`Tender PDF → Structured Extraction → Evidence Retrieval → Compliance Analysis → Human Decision`

The system is designed around specialized graph nodes rather than a single unconstrained LLM prompt.

## Current Scope

### Phase 1 — Discovery

Find relevant tenders across procurement portals.

**Status:** outside the current repository.

### Phase 2 — Tender Intelligence

Read the tender, extract relevant information and prepare compliance analysis.

**Status:** implemented as the current prototype.

### Phase 3 — Preparation

Potential future capabilities:

- proposal preparation;
- qualification checklist;
- clarification / objection drafting;
- commercial worksheet.

### Phase 4 — Participation

Potential future capabilities:

- procurement-session assistance;
- interaction support;
- portal workflow integration.

### Phase 5 — Post-session

Potential future capabilities:

- appeals;
- diligence;
- award / homologation tracking.

## Architecture

The current graph separates responsibilities:

1. **Reading / extraction** — converts the tender into structured information.
2. **Retrieval** — obtains relevant legal or reference evidence.
3. **Compliance analysis** — compares requirements against the retrieved evidence.
4. **Decision support** — surfaces findings for human review.

This separation is intentional.

> **Retrieval provides evidence; the LLM provides reasoning; the human remains responsible for the final decision.**

## Why LangGraph?

LangGraph provides an explicit stateful workflow where each step can be inspected, tested and extended.

Instead of treating the model as a black box, the project uses a graph structure to make the processing stages visible and replaceable.

That architecture creates a path toward:

- conditional routing;
- human-in-the-loop review;
- tool calling;
- retrieval augmentation;
- structured outputs;
- auditability.

## Repository Structure

```text
src/
  state.py
  graph.py
  nodes/
    leitura.py
    conformidade.py
  rag/
data/
  editais/       # local examples, not versioned
  legislacao/    # local legal corpus, not versioned
tests/
  test_state.py
```

## Technology Stack

- Python
- LangGraph
- Anthropic API / Claude
- ChromaDB
- RAG / vector retrieval
- PDF document processing
- Structured extraction
- Agentic workflow design

## Run Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it according to your operating system and install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Add the required API credentials, place a local example tender in `data/editais/exemplo.pdf`, and run:

```bash
python -m src.graph
```

## Roadmap

- [x] Stateful LangGraph architecture
- [x] Tender information extraction
- [x] Tool-assisted / vision-based PDF extraction
- [ ] Production-grade retrieval against Law 14.133/2021
- [ ] Evidence-linked compliance findings
- [ ] Conditional routing for non-compliance
- [ ] Human-in-the-loop review
- [ ] Full procurement workflow

## Evaluation & Trust

For a procurement assistant, a fluent answer is not enough.

A stronger evaluation framework should measure:

- extraction accuracy;
- retrieval relevance;
- evidence coverage;
- requirement-level classification accuracy;
- false positives / false negatives;
- citation or source traceability;
- human review agreement.

Legal interpretation should always be validated against authoritative sources and qualified professional review when required.

## Privacy & Security

Tender documents may contain commercially sensitive information.

Production deployments should apply:

- controlled document access;
- secret management;
- logging and audit trails;
- data-retention policies;
- model/provider governance;
- protection against prompt injection in retrieved documents.

No sensitive production documents should be committed to this repository.

## Limitations

This is a portfolio prototype, not a legal-advice system or autonomous bidding agent.

The current implementation focuses on the intelligence layer and does not execute bids, submit proposals or make binding legal decisions.

## Portfolio Perspective

This project demonstrates an applied AI pattern that is useful beyond procurement:

**Unstructured Documents → Structured Facts → Evidence Retrieval → AI Reasoning → Human Decision**

The central engineering goal is not to make the LLM autonomous. It is to make AI **useful, inspectable and grounded in evidence**.