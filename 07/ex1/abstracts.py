from ex0 import Creature
from abc import ABC, abstractmethod
from enum import Enum


class CreatureType(Enum):
    NORMAL = 'normal'
    BOSS = 'boss'


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.creatureType: CreatureType = CreatureType.NORMAL

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
