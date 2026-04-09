"""Our spell card module"""
from ex0.Card import Card
from enum import Enum


class Effect(Enum):
    DAMAGE = "Deal 3 damage to target"
    HEAL = "+5 health points"
    BUFF = "Permanent: +1 mana per turn"
    DEBUFF = "-2 mana to your enemies"


class SpellCard(Card):
    """Spell card class"""

    def __init__(
        self,
        name: str,
        cost: str,
        rarity: str,
        effect_type: Effect,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.stats["effect"] = effect_type.value

    def play(self, game_state: dict) -> dict:
        """Play the spell card and update `game_state`."""
        game_state["card_played"] = self.stats["name"]
        game_state["mana_used"] = self.stats["cost"]
        game_state["effect"] = self.effect_type.value
        return game_state

    def resolve_effect(self, targets: list[Card]) -> dict:
        """Apply this spell's effect to the provided targets."""
        if not targets:
            return {
                "spell": self.stats["name"],
                "effect_type": self.effect_type.name,
                "targets": 0,
                "results": [],
            }

        results: list[dict[str, object]] = []

        for target in targets:
            stats = target.stats
            target_name = str(stats.get("name", ""))

            if self.effect_type == Effect.DAMAGE:
                before = int(stats.get("health", 0))
                stats["health"] = before - 3
                results.append(
                    {
                        "target": target_name,
                        "type": "damage",
                        "amount": 3,
                        "health_before": before,
                        "health_after": stats["health"],
                    }
                )

            elif self.effect_type == Effect.HEAL:
                before = int(stats.get("health", 0))
                stats["health"] = before + 5
                results.append(
                    {
                        "target": target_name,
                        "type": "heal",
                        "amount": 5,
                        "health_before": before,
                        "health_after": stats["health"],
                    }
                )

            elif self.effect_type == Effect.BUFF:
                before = int(stats.get("mana_per_turn", 0))
                stats["mana_per_turn"] = before + 1
                results.append(
                    {
                        "target": target_name,
                        "type": "buff",
                        "stat": "mana_per_turn",
                        "delta": 1,
                        "before": before,
                        "after": stats["mana_per_turn"],
                    }
                )

            elif self.effect_type == Effect.DEBUFF:
                before = int(stats.get("mana_per_turn", 0))
                stats["mana_per_turn"] = before - 2
                results.append(
                    {
                        "target": target_name,
                        "type": "debuff",
                        "stat": "mana_per_turn",
                        "delta": -2,
                        "before": before,
                        "after": stats["mana_per_turn"],
                    }
                )

        return {
            "spell": self.stats["name"],
            "effect_type": self.effect_type.name,
            "targets": len(targets),
            "results": results,
        }
