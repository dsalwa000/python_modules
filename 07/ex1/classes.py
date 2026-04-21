from ex0 import Creature, CreatureFactory
from .abstracts import HealCapability, TransformCapability
from .abstracts import CreatureType


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals {target.name} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: Creature | None = None) -> str:
        if target is None:
            return f"{self.name} heals itself for a large amount"
        else:
            return f"{self.name} heals {target.name} for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name=name, type=type)

    def attack(self) -> str:
        if self.creatureType == CreatureType.NORMAL:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        if self.creatureType == CreatureType.NORMAL:
            self.creatureType = CreatureType.BOSS
            return "Shiftling shifts into a sharper form!"
        else:
            return "You are already the boss"

    def revert(self) -> str:
        if self.creatureType == CreatureType.BOSS:
            self.creatureType = CreatureType.NORMAL
            return "Shiftling returns to normal."
        else:
            return "You are already normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        if self.creatureType == CreatureType.NORMAL:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        if self.creatureType == CreatureType.NORMAL:
            self.creatureType = CreatureType.BOSS
            return "Morphagon morphs into a dragonic battle form!"
        else:
            return "You are already the boss"

    def revert(self) -> str:
        if self.creatureType == CreatureType.BOSS:
            self.creatureType = CreatureType.NORMAL
            return "Morphagon returns to normal."
        else:
            return "You are already normal"


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
