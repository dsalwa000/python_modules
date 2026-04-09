"""Our Artifact Card module"""
from ex0.Card import Card
from ex1.SpellCard import Effect


class ArtifactCard(Card):
    """Our Artifact Card class"""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: Effect,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.stats["durability"] = durability
        self.stats["effect"] = effect.value
        self.effect_type = effect

    def play(self, game_state: dict) -> dict:
        """Play the artifact card and update `game_state`."""
        game_state["card_played"] = self.stats["name"]
        game_state["mana_used"] = self.stats["cost"]
        result = self.activate_ability()
        game_state["effect"] = result["effect"]
        return game_state

    def activate_ability(self) -> dict:
        """Activate the artifact ability and decrease durability."""
        durability = int(self.stats.get("durability", 0))
        if durability <= 0:
            return {
                "artifact": self.stats["name"],
                "activated": False,
                "effect": "Artifact is broken (durability = 0)",
                "durability": 0,
            }

        durability -= 1
        self.stats["durability"] = durability

        return {
            "artifact": self.stats["name"],
            "activated": True,
            "effect": self.effect_type.value,
            "durability": durability,
        }
