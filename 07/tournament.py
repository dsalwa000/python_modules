from ex0 import FlameFactory, AquaFactory, Creature
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


class TournamentError(Exception):
    """It catches tournament errors"""
    pass


"""Normal creatures"""
flameFactory = FlameFactory()
aquaFactory = AquaFactory()

flameling = flameFactory.create_base()
pyrodon = flameFactory.create_evolved()
aquabub = aquaFactory.create_base()
torragon = aquaFactory.create_evolved()

"""Aggressive creatures"""
transformCreatureFactory = TransformCreatureFactory()

shiftling = transformCreatureFactory.create_base()
morphagon = transformCreatureFactory.create_evolved()

"""Defensive creatures"""
healingCreatureFactory = HealingCreatureFactory()

sproutling = healingCreatureFactory.create_base()
bloomelle = healingCreatureFactory.create_evolved()

"""Figth tuples"""
normalFight: tuple[Creature] = (
    flameling,
    pyrodon,
    aquabub,
    torragon
)

aggressiveFigth: tuple[Creature] = (
    shiftling,
    morphagon
)

defensiveFight: tuple[Creature] = (
    sproutling,
    bloomelle
)

"""Strategies"""
normal = NormalStrategy()
aggressive = AggressiveStrategy()
defensive = DefensiveStrategy()


"""Let the games begins"""
print("Tournament 0 (basic)")
print(normal.act(normalFight))

print("\nTournament 1 (error)")
print(normal.act((shiftling, morphagon)))

print("\nTournament 2 (multiple)")
print(aggressive.act(aggressiveFigth))

print("\nTournament 3 (error)")
print(aggressive.act(normalFight))

print("\nTournament 4 (multiple)")
print(defensive.act(defensiveFight))

print("\nTournament 5 (error)")
print(defensive.act(aggressiveFigth))
