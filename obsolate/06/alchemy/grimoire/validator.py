"""Let's validate"""


def validate_ingredients(ingredients: str) -> str:
    """
    It tells if ingridents are correct.
    List of correct ingredients: fire, water, earth and air

    Args:
        ingredients (str) - it should be a stirng of valid ingredients
        separated by spaces

    """
    ingredients_list: list[str] = ingredients.split()
    valid_ingredients = {"fire", "water", "earth", "air"}

    for ing in ingredients_list:
        if ing not in valid_ingredients:
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"
