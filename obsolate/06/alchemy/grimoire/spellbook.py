"""Let's spell"""


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    This funciton uses validator and spells record
    """
    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)

    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
