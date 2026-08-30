from typing import List, Optional

from pydantic import BaseModel, Field


class DadosEdital(BaseModel):
    """Dados estruturados extraídos de um edital de licitação.

    Esse é o "formato" que pedimos ao Claude para preencher a partir do
    texto bruto do PDF — em vez de um bloco de texto livre, ganhamos um
    objeto com campos previsíveis que os próximos nós (conformidade,
    precificação) podem ler diretamente.
    """

    objeto: str = Field(description="O que está sendo licitado, em poucas palavras")
    orgao: Optional[str] = Field(default=None, description="Órgão público responsável")
    valor_estimado: Optional[str] = Field(default=None, description="Valor estimado, se informado")
    prazo_entrega_propostas: Optional[str] = Field(default=None, description="Prazo limite para envio de propostas")
    exigencias_habilitacao: List[str] = Field(default_factory=list, description="Principais exigências de habilitação")