"""Light"""


def light_spell_allowed_ingredients() -> list[str]:
    return ["fire", "earth", "water", "air"]


def light_spell_record(spell_name: str, ingredients: str):
    if spell_name == "good" and ingredients == "nice":
        return "Recorded"

    return "Rejected"
