"""ex2.EliteCard"""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Playable card class implementation"""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Create a new elite card

        """
        super().__init__(name, cost, rarity)
        self._health: int = 8
        self._armor: int = 3
        self._attack: int = int(cost)
        self._mana: int = 4

    def play(self, game_state: dict) -> dict:

        result = {
            "card_played": self.stats.get("name"),
            "mana_used": self.stats.get("cost", 0),
            "effect": "elite_play",
        }
        if isinstance(game_state, dict):
            game_state.update(result)
        return result

    def attack(self, target) -> dict:
        """I have a plan, attack"""
        target_name = getattr(target, "stats", {}).get("name", str(target))

        return {
            "attacker": self.stats.get("name"),
            "target": target_name,
            "damage": self._attack,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage

        Args:
            incoming_damage: Damage value to mitigate

        Returns:
            A dictionary describing the defense result
        """
        blocked = min(self._armor, max(0, int(incoming_damage)))
        taken = max(0, int(incoming_damage) - blocked)
        self._health = max(0, self._health - taken)

        return {
            "defender": self.stats.get("name"),
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self._health > 0,
        }

    def get_combat_stats(self) -> dict:
        """Return current combat-related stats"""
        return {
            "attack": self._attack,
            "health": self._health,
            "armor": self._armor,
        }

    def cast_spell(self, spell_name: str, targets: list):
        """Cast a spell on the provided targets.

        Args:
            spell_name: Name of the spell.
            targets: List of cards which are targets

        Returns:
            A dictionary describing the spell cast
        """
        mana_used = 4 if spell_name == "Fireball" else 1

        names: list[str] = []
        for target in targets:
            names.append(target)

        return {
            "caster": self.stats.get("name"),
            "spell": spell_name,
            "targets": names,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int):
        """Increase internal mana pool by amount

        Args:
            amount: Mana to add

        Returns:
            A dictionary with the amount channeled and current total mana
        """
        self._mana += int(amount)
        return {
            "channeled": int(amount),
            "total_mana": self._mana,
        }

    def get_magic_stats(self):
        """Return current magic-related stats (currently only mana)"""
        return {
            "mana": self._mana,
        }
