"""The card"""
from __future__ import annotations
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, ranking: int):
        """
        record: is a double table - [wins, loses]

        """
        super().__init__(name, cost, rarity)
        self.ranking = ranking
        self.record = [0, 0]
        self.armor = 5

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.stats["name"]
        game_state["mana_used"] = self.stats["cost"]
        game_state["effect"] = self.stats["effect"]
        return game_state

    def attack(self, target: TournamentCard) -> dict:
        """If a rangking of your card is higher you will win"""
        if target.ranking < self.ranking:
            self.record[0] += 1
            target.record[1] += 1
        else:
            self.record[1] += 1
            target.record[0] += 1

        return self.get_tournament_stats()

    def defend(self, incoming_damage: int) -> dict:
        """
        We can defend ourselfs if the incoming damage is lower or equal
        than our armor

        """
        saved = True

        if self.armor < incoming_damage:
            self.record[1] += 1
            saved = False

        return {
            "armor": self.armor,
            "attack": incoming_damage,
            "saved": saved
        }

    def calculate_rating(self) -> int:
        return self.ranking

    def get_tournament_stats(self) -> dict:
        return {
            "wins": self.record[0],
            "losses": self.record[1]
        }

    def update_wins(self, wins: int) -> None:
        self.record[0] += wins

    def update_losses(self, losses: int) -> None:
        self.record[0] += losses

    def get_rank_info(self) -> dict:
        return {
            "ranking": self.ranking,
        }

    def get_combat_stats(self) -> dict:
        return {
            "balance": self.record
        }
