"""
Schema for pokemons.
"""
from voluptuous import Schema, PREVENT_EXTRA

pokemon_create = Schema(
    {
        "id": str,
        "message":str
    },
    extra=PREVENT_EXTRA,
    required=True
)

