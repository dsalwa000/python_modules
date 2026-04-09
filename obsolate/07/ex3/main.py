"""This program shows how the factory class works"""

from __future__ import annotations

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AgressiveStrategy
from ex3.GameEngine import Engine

print("=== DataDeck Game Engine ===\n")

print("Configuring Fantasy Card Game...")
print("Factory: FantasyCardFactory")
print("Strategy: AggressiveStrategy")

factory = FantasyCardFactory()
strategy = AgressiveStrategy()
engine = Engine()
engine.configure_engine(factory, strategy)

print(f"Available types: {factory.get_supported_types()}")

print("Simulating aggressive turn...")
print(f"Hand: {engine.hand}")

print("\nTurn execution")
print(f"Strategy: {engine.strategy.get_strategy_name()}")
print(f"Actions: {engine.simulate_turn()}")

print("\nGame Report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
