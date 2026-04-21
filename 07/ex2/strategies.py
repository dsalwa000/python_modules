from .BattleStrategy import BattleStrategy
from ex0 import Creature


class NormalStrategy(BattleStrategy):
    """
    This class allows us to make a battle normal cards

    """
    def is_valid(self, creatures: tuple[Creature]) -> bool:
        allowed = {"Flameling", "Pyrodon", "Aquabub", "Torragon"}
        for creature in creatures:
            if (
                creature.__class__.__name__ not in allowed
                or creature.__class__.__name__ not in allowed
            ):
                return False

        return True

    def act(self, creatures: tuple[Creature]) -> str:
        if not self.is_valid(creatures):
            return "Fight failed"

        fights: list[str] = []
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                attacker = creatures[i]
                defender = creatures[j]
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
    def is_valid(self, creatures: tuple[Creature]) -> bool:
        allowed = {"Shiftling", "Morphagon"}
        for creature in creatures:
            if (
                creature.__class__.__name__ not in allowed
                or creature.__class__.__name__ not in allowed
            ):
                return False

        return True

    def act(self, creatures: tuple[Creature]) -> str:
        if not self.is_valid(creatures):
            return "Fight failed"

        fights: list[str] = []
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                attacker = creatures[i]
                defender = creatures[j]
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
    def is_valid(self, creatures: tuple[Creature]) -> bool:
        allowed = {"Sproutling", "Bloomelle"}
        for creature in creatures:
            if (
                creature.__class__.__name__ not in allowed
                or creature.__class__.__name__ not in allowed
            ):
                return False

        return True

    def act(self, creatures: tuple[Creature]) -> str:
        if not self.is_valid(creatures):
            return "Fight failed"

        fights: list[str] = []
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                attacker = creatures[i]
                defender = creatures[j]
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
