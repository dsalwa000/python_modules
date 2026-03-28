"""Our real factory"""
from __future__ import annotations

import random

from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import Effect, SpellCard
from ex1.Deck import Deck


class FantasyCardFactory(CardFactory):
    """Concrete factory producing a small set of fantasy-themed cards."""

    _CREATURE_POOL: list[dict[str, object]] = [
        {
            "name": "Goblin Raider",
            "cost": 1,
            "rarity": "Common",
            "attack": 2,
            "health": 1,
        },
        {
            "name": "Elven Archer",
            "cost": 2,
            "rarity": "Common",
            "attack": 2,
            "health": 2,
        },
        {
            "name": "Dwarven Defender",
            "cost": 3,
            "rarity": "Rare",
            "attack": 1,
            "health": 5,
        },
        {
            "name": "Dragon Whelp",
            "cost": 4,
            "rarity": "Epic",
            "attack": 5,
            "health": 3,
        },
    ]

    _SPELL_POOL: list[dict[str, object]] = [
        {
            "name": "Fireball",
            "cost": 2,
            "rarity": "Common",
            "effect": Effect.DAMAGE,
        },
        {
            "name": "Healing Light",
            "cost": 2,
            "rarity": "Common",
            "effect": Effect.HEAL,
        },
        {
            "name": "Arcane Wisdom",
            "cost": 3,
            "rarity": "Rare",
            "effect": Effect.BUFF,
        },
        {
            "name": "Curse of Weakness",
            "cost": 3,
            "rarity": "Rare",
            "effect": Effect.DEBUFF,
        },
    ]

    _ARTIFACT_POOL: list[dict[str, object]] = [
        {
            "name": "Runed Amulet",
            "cost": 2,
            "rarity": "Common",
            "durability": 2,
            "effect": Effect.BUFF,
        },
        {
            "name": "Poisoned Dagger",
            "cost": 2,
            "rarity": "Common",
            "durability": 3,
            "effect": Effect.DAMAGE,
        },
        {
            "name": "Holy Relic",
            "cost": 3,
            "rarity": "Rare",
            "durability": 2,
            "effect": Effect.HEAL,
        },
        {
            "name": "Shadow Idol",
            "cost": 4,
            "rarity": "Epic",
            "durability": 1,
            "effect": Effect.DEBUFF,
        },
    ]

    def _pick_from_pool(
        self, pool: list[dict[str, object]]
    ) -> dict[str, object]:
        return dict(random.choice(pool))

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a CreatureCard.

        - None: pick a random predefined creature from the pool.
        - str: create a randomized creature with the provided name.
        - int: create a randomized creature with a default name
          and given attack.
        """
        if name_or_power is None:
            creature = self._pick_from_pool(self._CREATURE_POOL)
            return CreatureCard(
                name=creature["name"],
                cost=creature["cost"],
                rarity=creature["rarity"],
                attack=creature["attack"],
                health=creature["health"],
            )

        cost = random.randint(1, 5)

        rarity_table = ["Legendary", "Unique", "Common"]
        rarity = random.choice(rarity_table)

        attack = random.randint(1, 6)
        health = random.randint(1, 6)

        if isinstance(name_or_power, str):
            return CreatureCard(
                name=name_or_power,
                cost=cost,
                rarity=rarity,
                attack=attack,
                health=health,
            )

        if isinstance(name_or_power, int):
            return CreatureCard(
                name="Nameless",
                cost=cost,
                rarity=rarity,
                attack=name_or_power,
                health=health,
            )

        raise TypeError("name_or_power must be str, int or None")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a SpellCard

        - str: name, default effect chosen from name hash.
        - int: treated as cost.
        - None: pick a random predefined spell.

        """
        if name_or_power is None:
            spell = self._pick_from_pool(self._SPELL_POOL)
            return SpellCard(
                name=spell["name"],
                cost=spell["cost"],
                rarity=spell["rarity"],
                effect_type=spell["effect"],
            )

        cost = str(random.randint(1, 5))

        rarity_table = ["Legendary", "Unique", "Common"]
        rarity = random.choice(rarity_table)

        effects = [Effect.BUFF, Effect.DAMAGE, Effect.DEBUFF, Effect.HEAL]
        effect = random.choice(effects)

        if isinstance(name_or_power, str):
            return SpellCard(
                name=name_or_power,
                cost=cost,
                rarity=rarity,
                effect_type=effect,
            )

        if isinstance(name_or_power, int):
            return SpellCard(
                name="Nameless",
                cost=str(name_or_power),
                rarity=rarity,
                effect_type=Effect.DAMAGE,
            )

        raise TypeError("name_or_power must be str, int or None")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        Create an ArtifactCard

        - None: pick a random predefined artifact from the pool
        - str: create a randomized artifact with the provided name
        - int: create a randomized artifact with a default name and given cost
        """
        if name_or_power is None:
            artifact = self._pick_from_pool(self._ARTIFACT_POOL)
            return ArtifactCard(
                name=artifact["name"],
                cost=artifact["cost"],
                rarity=artifact["rarity"],
                durability=artifact["durability"],
                effect=artifact["effect"],
            )

        cost = random.randint(1, 5)

        rarity_table = ["Legendary", "Unique", "Common"]
        rarity = random.choice(rarity_table)

        effects = [Effect.BUFF, Effect.DAMAGE, Effect.DEBUFF, Effect.HEAL]
        effect = random.choice(effects)

        durability = random.randint(1, 3)

        if isinstance(name_or_power, str):
            return ArtifactCard(
                name=name_or_power,
                cost=cost,
                rarity=rarity,
                durability=durability,
                effect=effect,
            )

        if isinstance(name_or_power, int):
            return ArtifactCard(
                name="Nameless",
                cost=name_or_power,
                rarity=rarity,
                durability=durability,
                effect=Effect.DAMAGE,
            )

        raise TypeError("name_or_power must be str, int or None")

    def create_themed_deck(self, size: int) -> dict:
        """
        Create a deck dict: {"deck": Deck, "stats": dict}

        The deck contains a mix of creatures/spells/artifacts
        """
        if size <= 0:
            raise ValueError("size must be > 0")

        deck = Deck()
        for _ in range(size):
            roll = random.random()
            if roll < 0.5:
                deck.add_card(self.create_creature())
            elif roll < 0.8:
                deck.add_card(self.create_spell())
            else:
                deck.add_card(self.create_artifact())

        deck.shuffle()
        return {"deck": deck, "stats": deck.get_deck_stats()}

    def get_supported_types(self) -> dict:
        """Return supported product types for this factory"""
        return {
            "creature": ['dragon', 'goblin'],
            "spell": ['fireball'],
            "artifact": ['mana_ring']
        }
