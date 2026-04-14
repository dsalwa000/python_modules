"""Let's validate light spells"""
from light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    valid_igredients: list[str] = light_spell_allowed_ingredients()

    if ingredients in valid_igredients:
        return "VALID"
    return "INVALID"
