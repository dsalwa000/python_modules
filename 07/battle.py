from ex0 import FlameFactory, AquaFactory

print("Testing factory")
flameFactory = FlameFactory()
flameling = flameFactory.create_base()
pyrodon = flameFactory.create_evolved()

print(flameling.describe(flameling))
print(flameling.attack())
print(pyrodon.describe(pyrodon))
print(pyrodon.attack())

print("\nTesting factory")
aquaFactory = AquaFactory()
aquabub = aquaFactory.create_base()
torragon = aquaFactory.create_evolved()

print(aquabub.describe(aquabub))
print(aquabub.attack())
print(torragon.describe(torragon))
print(torragon.attack())

print("\nTesting battle")
print(flameling.describe(flameling))
print("vs")
print(torragon.describe(torragon))
print(flameling.attack())
print(torragon.attack())
