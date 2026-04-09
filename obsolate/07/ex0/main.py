"""Cards demonstration"""
from ex0.CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")

# Our cards
try:
    fire_dragon = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )
    goblin_warrior = CreatureCard(
        "Goblin Warrior",
        1,
        "Not Legendary at all",
        1,
        1
    )
except ValueError as e:
    print(e)

print("CreatureCard Info:")
print(fire_dragon.get_card_info())

# Empty game_state means that there is no move done yet
available_mana: int = 6
game_state: dict[str, object] = {
    "card_played": "",
    "mana_used": 0,
    "effect": ""
}

print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable: {fire_dragon.is_playable(available_mana)}")

fire_dragon.play(game_state)
print(f"Play result: {game_state}")

print("\nFire Dragon attacks Goblin Warrior:")

attack_result: dict[str, object] = fire_dragon.attack_target(goblin_warrior)
available_mana -= fire_dragon.stats["cost"]
print(f"Attack result: {attack_result}")

print(f"\nTesting insufficient mana ({available_mana} available):")
print(f"Playable: {fire_dragon.is_playable(available_mana)}")

print("\nAbstract pattern successfully demonstrated!")
