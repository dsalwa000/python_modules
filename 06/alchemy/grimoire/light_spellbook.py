def light_spell_allowed_ingredients() -> list[str]:
    return ["fire", "earth", "water", "air"]


def light_spell_record(spell_name: str, ingredients: str):
    from .light_validator import validate_ingredients

    validator = validate_ingredients(ingredients)

    if validator == "VALID":
        return spell_name
    elif validator == "INVALID":
        return "Spell not recorded"
