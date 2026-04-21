from ex1 import TransformCreatureFactory, HealingCreatureFactory

healingCreatureFactory = HealingCreatureFactory()
transformCreatureFactory = TransformCreatureFactory()

print("Testing Creature with healing capability:")

sproutling = healingCreatureFactory.create_base()
bloomelle = healingCreatureFactory.create_evolved()

print(sproutling.describe(sproutling))
print(sproutling.attack())
print(sproutling.heal())
print(sproutling.heal(bloomelle))

print("\nEvolved:")
print(bloomelle.describe(bloomelle))
print(bloomelle.attack())
print(bloomelle.heal())
print(bloomelle.heal(sproutling))

print("\nTesting Creature with transform capability:")

shiftling = transformCreatureFactory.create_base()
morphagon = transformCreatureFactory.create_evolved()

print(shiftling.describe(shiftling))
print(shiftling.attack())
print(shiftling.transform())
print(shiftling.attack())
print(shiftling.revert())
print(morphagon.attack())

print("\nEvolved:")
print(morphagon.describe(morphagon))
print(morphagon.attack())
print(morphagon.transform())
print(morphagon.attack())
print(morphagon.revert())
print(morphagon.attack())
