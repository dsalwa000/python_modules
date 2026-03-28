"""The card"""
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self.tournament_cards: list[TournamentCard] = []
        self.battles = 0

    def register_card(self, card: TournamentCard) -> str:
        self.tournament_cards.append(card)

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """card_id is a name of a card"""
        card1: TournamentCard = None
        card2: TournamentCard = None

        for card in self.tournament_cards:
            if card.stats["name"] == card1_id:
                card1 = card
                break

        for card in self.tournament_cards:
            if card.stats["name"] == card2_id:
                card2 = card
                break

        self.battles += 1
        stats = card1.attack(card2)
        return stats

    def get_leaderboard(self) -> list:
        return self.tournament_cards

    def generate_tournament_report(self) -> dict:
        return {
            "cards": self.tournament_cards,
            "amount_of_cards": len(self.tournament_cards),
            "battles": self.battles
        }
