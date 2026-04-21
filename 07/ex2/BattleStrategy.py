from abc import ABC, abstractmethod
from ex0 import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creatures: tuple[Creature]) -> bool:
        pass

    @abstractmethod
    def act(self, creatures: tuple[Creature]) -> str:
        pass
