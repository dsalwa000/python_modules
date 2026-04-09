"""Gold"""
from alchemy.potions import strength_potion
from elements import create_fire
from ..elements import create_air


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and "
        f"'{strength_potion()}' mixed with "
        f"'{create_fire()}'"
    )
