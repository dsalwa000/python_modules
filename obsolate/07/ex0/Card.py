"""Abstract class for our game"""
from abc import ABC, abstractmethod


class Card(ABC):
    """
    Abstract class for our cards

    """
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.stats: dict[str, object] = {
            "name": name,
            "cost": cost,
            "rarity": rarity,
        }

    def __str__(self) -> str:
        return self.stats["name"]

    __repr__ = __str__

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Method which shows how playing a specific card works

        """
        pass

    def get_card_info(self) -> dict:
        return dict(self.stats)

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= int(self.stats.get("cost", 0))
