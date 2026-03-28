"""Let's combine everything we learned in this module"""
from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard

print("=== DataDeck Tournament Platform ===\n")

print("Registering Tournament Cards...\n")

platform = TournamentPlatform()
fire_dragon = TournamentCard("Fire Dragon", 4, "Rare", 1200)
ice_wizard = TournamentCard("Ice Wizard", 4, "Not Rare", 900)

platform.register_card(fire_dragon)
platform.register_card(ice_wizard)

print(f"Starting report: {platform.generate_tournament_report()}")

print("Create tournament match")
print(f"Stats: {platform.create_match('Fire Dragon', 'Ice Wizard')}")
print(f"Board {platform.get_leaderboard()}")
print(f"Tournament report: {platform.generate_tournament_report()}")

fire_dragon = TournamentCard("Fire Dragon", 4, "Rare", 1200)

print("\n=== Tournament Platform Successfully Deployed! ===")
