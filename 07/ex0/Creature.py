from abc import ABC, abstractmethod
from typing import TypeVar


T = TypeVar('T', bound='Creature')


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self, creature: T) -> str:
        return f"{creature.name} is a {creature.type} creature."
