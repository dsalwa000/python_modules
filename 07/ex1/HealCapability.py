from ..ex0 import Creature
from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature):
        pass

