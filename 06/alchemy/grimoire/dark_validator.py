"""Let's validate dark spells"""
from dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    valid_igredients: list[str] = dark_spell_allowed_ingredients()

    if ingredients in valid_igredients:
        return "VALID"
    return "INVALID"
