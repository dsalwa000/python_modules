from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act() -> None:
        pass

    @abstractmethod
    def is_valid() -> bool:
        pass
