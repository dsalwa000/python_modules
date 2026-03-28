"""Engine"""

from __future__ import annotations

from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard

enemy = CreatureCard(
    "Enemy",
    1,
    "Not Legendary at all",
    1,
    1
)


class Engine:
    """Small game engine that wires a CardFactory with a GameStrategy"""

    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.deck: Deck | None = None
        self.hand: list[Card] = []
        self.turns_simulated = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        """
        Attach factory and strategy

        Creating a deck and draw 5 cards to hand

        """
        self.factory = factory
        self.strategy = strategy

        our_deck = self.factory.create_themed_deck(10)
        self.deck = our_deck["deck"]

        for _ in range(5):
            self.hand.append(self.deck.draw_card())

    def simulate_turn(self) -> dict:
        self.turns_simulated += 1
        return self.strategy.execute_turn(self.hand, [enemy])

    def get_engine_status(self) -> dict:
        """Returns game report"""
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "cards_left_in_deck": len(self.deck.cards)
        }
