"""
We will be playing with different types of cards
using a whole deck

"""
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, Effect
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

print("=== DataDeck Deck Builder ===\n")

deck = Deck()

# Empty game_state means that there is no move done yet
available_mana: int = 6
game_state: dict[str, object] = {
    "card_played": "",
    "mana_used": 0,
    "effect": ""
}

# Our cards
lightning_bolt = SpellCard(
    "Lightning Bolt",
    5,
    "Cool",
    Effect.DAMAGE
)
mana_cristal = ArtifactCard(
    "Lightning Bolt",
    5,
    "Normal",
    10,
    Effect.BUFF
)
fire_dragon = CreatureCard(
    "Fire Dragon",
    5,
    "Legendary",
    7,
    5
)

deck.add_card(lightning_bolt)
deck.add_card(mana_cristal)
deck.add_card(fire_dragon)

print("Building deck with different card types...\n")
print(f"Deck stats: {deck.get_deck_stats()}")

print("Drawing and playing cards:\n")
deck.shuffle()

drew: Card = deck.draw_card()
print(f"Drew: {drew.stats['name']}")
print(f"Played: {drew.play(game_state)}")

drew = deck.draw_card()
print(f"Drew: {drew.stats['name']}")
print(f"Played: {drew.play(game_state)}")

drew = deck.draw_card()
print(f"Drew: {drew.stats['name']}")
print(f"Played: {drew.play(game_state)}")

print("\nPolymorphism in action: Same interface, different card behaviors!")
