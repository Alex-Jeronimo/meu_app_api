# Este arquivo reúne os schemas em um único ponto de importação.
# Assim, as rotas podem importar de `schemas` sem conhecer a estrutura interna da pasta.
from schemas.atividade import (
    AtividadeDelSchema,
    AtividadeFiltroSchema,
    AtividadePathSchema,
    AtividadeSchema,
    AtividadeUpdateSchema,
    AtividadeViewSchema,
    ListagemAtividadesSchema,
    apresenta_atividade,
    apresenta_atividades,
    calcula_dias_restantes,
)
from schemas.error import ErrorSchema
