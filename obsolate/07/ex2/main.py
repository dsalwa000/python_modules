"""Let's see how double abstract works"""
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===")

print("EliteCard capabilities:")
print(f"- Card: {list(Card.__abstractmethods__)}")
print(f"- Combatable: {list(Combatable.__abstractmethods__)}")
print(f"- Magical: {list(Magical.__abstractmethods__)}")

print("Playing Arcane Warrior (Elite Card):\n")

eliteCard = EliteCard("Arcane Warrior", 5, "Elite")
targetCard1 = EliteCard("Enemy1", 8, "Elite but worse")
targetCard2 = EliteCard("Enemy2", 8, "Elite but worse")

print("Combat phase:")
print(f"Attack result: {eliteCard.attack(targetCard1)}")
print(f"Defense result: {eliteCard.defend(5)}")

print("Magic phase:")
spell_result = eliteCard.cast_spell("Fireball", [targetCard1, targetCard2])
print(f"Spell cast: {spell_result}")
print(f"Mana channel: {eliteCard.channel_mana(3)}")

print("Multiple interface implementation successful!")
