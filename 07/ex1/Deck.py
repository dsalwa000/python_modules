"""The deck"""
from ex0.Card import Card
import random


class Deck:
    """
    Using this class you can create a deck which contains many
    different types of cards

    You can add, remove, shuffle, draw card and get deck status
    """

    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Returs:
            bool: True when delation was successful, False when failed
        """
        for card in self.cards:
            if card_name == card.stats["name"]:
                self.cards.remove(card_name)
                return True

        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)
        print("The deck was shuffled\n")

    def draw_card(self) -> Card:
        """We return one single card and removes it from the deck"""
        card: Card = self.cards[0]
        self.cards.remove(card)

        return card

    def get_deck_stats(self) -> dict:
        """Return a summary of the deck as a dict (easy to print/test)."""
        names: list[str] = []
        by_rarity: dict[str, int] = {}
        total_cost: int = 0

        for card in self.cards:
            stats = card.get_card_info()
            name = stats.get("name", "")
            rarity = stats.get("rarity", "Unknown")
            cost = stats.get("cost", 0)

            if name:
                names.append(name)
            by_rarity[rarity] = by_rarity.get(rarity, 0) + 1
            total_cost += cost

        count = len(self.cards)
        avg_cost = (total_cost / count) if count else 0.0

        return {
            "count": count,
            "names": names,
            "by_rarity": by_rarity,
            "avg_cost": avg_cost,
        }
