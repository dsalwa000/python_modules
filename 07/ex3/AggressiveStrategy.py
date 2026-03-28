"""It should be agressive"""

from __future__ import annotations

from ex0.CreatureCard import CreatureCard


class AgressiveStrategy:
    """Aggressive strategy focused on damage and board presence."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Execute an aggressive turn.

        Args:
            hand: card you hava
            battlefield: list of your enemies
        """
        attacks: int = 0
        playable_cards: list[CreatureCard] = []

        for card in hand:
            if isinstance(card, CreatureCard):
                playable_cards.append(card)

        for card in playable_cards:
            for enemy in battlefield:
                attacks += 1
                card.attack_target(enemy)

        return {
            "cards_played": playable_cards,
            "attacks": attacks,
            "targets_attacked": battlefield
        }

    def prioritize_targets(self, available_targets: list) -> list:
        """Just provide a list of prioritized targets"""
        return available_targets

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"
