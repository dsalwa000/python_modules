from typing import List

from .elements import create_air
from .potions import healing_potion as heal, strength_potion
from . import transmutation
from . import grimoire

__version__: str = "1.0.0"
__author__: str = "Magic"
__all__: List[str] = [
    "transmutation",
    "create_air",
    "heal",
    "strength_potion",
    "grimoire"
]
