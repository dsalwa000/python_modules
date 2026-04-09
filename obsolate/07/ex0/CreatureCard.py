"""Our real card"""
from ex0.Card import Card


class CreatureCard(Card):
    """
    This is a class which represents card to play

    """
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack or health are 0 or less")
        self.stats["attack"] = attack
        self.stats["health"] = health
        self.stats["effect"] = "Creature summoned to battlefield"

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.stats["name"]
        game_state["mana_used"] = self.stats["cost"]
        game_state["effect"] = self.stats["effect"]
        return game_state

    def attack_target(self, target: Card) -> dict:
        """This method uses mana and attacks different card"""
        target.stats["health"] -= self.stats["attack"]

        attact_result = {
            "attacker": self.stats["name"],
            "target": target.stats["name"],
            "damage_dealt": self.stats["attack"],
            "combat_resolved": True
        }

        return attact_result
