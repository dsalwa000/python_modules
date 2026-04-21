from typing import TypeAlias
from .BattleStrategy import BattleStrategy
from ex0 import Creature
from ex0.creatures import Flameling, Pyrodon, Aquabub, Torragon
from ex1.classes import (
    Sproutling,
    Bloomelle,
    Shiftling,
    Morphagon
)

NormalBattleCreature: TypeAlias = Flameling | Pyrodon | Aquabub | Torragon
TransformBattleCreature: TypeAlias = Shiftling | Morphagon
HealingBattleCreature: TypeAlias = Sproutling | Bloomelle


class NormalStrategy(BattleStrategy):
    """
    This class allows us to make a battle normal cards

    """
    def is_valid(self, creatures: tuple[Creature, ...]) -> bool:
        return all(
            isinstance(creature, (Flameling, Pyrodon, Aquabub, Torragon))
            for creature in creatures
        )

    def act(self, creatures: tuple[Creature, ...]) -> str:
        if not self.is_valid(creatures):
            return "Fight failed"

        fights: list[str] = []
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                attacker = creatures[i]
                defender = creatures[j]
                assert isinstance(
                    attacker,
                    (Flameling, Pyrodon, Aquabub, Torragon)
                )
                assert isinstance(
                    defender,
                    (Flameling, Pyrodon, Aquabub, Torragon)
                )
                fights.append(
                    "\n".join(
                        [
                            attacker.describe(attacker),
                            "vs",
                            defender.describe(defender),
                            attacker.attack(),
                            defender.attack(),
                        ]
                    )
                )

        return "\n\n".join(fights)


class AggressiveStrategy(BattleStrategy):
    """
    This class allows us to make a battle only for transform type of Creatures

    """
    def is_valid(self, creatures: tuple[Creature, ...]) -> bool:
        return all(
            isinstance(creature, (Shiftling, Morphagon))
            for creature in creatures
        )

    def act(self, creatures: tuple[Creature, ...]) -> str:
        if not self.is_valid(creatures):
            return "Fight failed"

        fights: list[str] = []
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                attacker = creatures[i]
                defender = creatures[j]
                assert isinstance(attacker, (Shiftling, Morphagon))
                assert isinstance(defender, (Shiftling, Morphagon))

                fights.append(
                    "\n".join(
                        [
                            attacker.describe(attacker),
                            "vs",
                            defender.describe(defender),
                            attacker.attack(),
                            attacker.transform(),
                            attacker.attack(),
                            defender.attack(),
                            defender.transform(),
                            defender.attack(),
                        ]
                    )
                )

        return "\n\n".join(fights)


class DefensiveStrategy(BattleStrategy):
    """
    This class allows us to make a battle only for healing type of Creatures

    """
    def is_valid(self, creatures: tuple[Creature, ...]) -> bool:
        return all(
            isinstance(creature, (Sproutling, Bloomelle))
            for creature in creatures
        )

    def act(self, creatures: tuple[Creature, ...]) -> str:
        if not self.is_valid(creatures):
            return "Fight failed"

        fights: list[str] = []
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                attacker = creatures[i]
                defender = creatures[j]
                assert isinstance(attacker, (Sproutling, Bloomelle))
                assert isinstance(defender, (Sproutling, Bloomelle))
                fights.append(
                    "\n".join(
                        [
                            attacker.describe(attacker),
                            "vs",
                            defender.describe(defender),
                            attacker.attack(),
                            attacker.heal(),
                            defender.attack(),
                            defender.heal()
                        ]
                    )
                )

        return "\n\n".join(fights)
