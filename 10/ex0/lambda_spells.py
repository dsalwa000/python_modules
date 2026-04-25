"""A file which demonstrate how a lambda works"""

"""Data genereted by data_generator"""
artifacts: list[dict[str, int | str]] = [
    {"name": "Wind Cloak", "power": 106, "type": "weapon"},
    {"name": "Fire Staff", "power": 117, "type": "relic"},
    {"name": "Earth Shield", "power": 115, "type": "focus"},
    {"name": "Shadow Blade", "power": 114, "type": "relic"},
]

mages: list[dict[str, int | str]] = [
    {"name": "Ember", "power": 76, "element": "water"},
    {"name": "Phoenix", "power": 50, "element": "fire"},
    {"name": "Rowan", "power": 87, "element": "light"},
    {"name": "Zara", "power": 54, "element": "earth"},
    {"name": "Kai", "power": 89, "element": "wind"},
]

spells: list[str] = [
    "shield",
    "tornado",
    "meteor",
    "heal",
]


def display(to_display: list) -> None:
    """Nothing fancy, just to display things"""

    for element in to_display:
        print(element)


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Let's sort"""
    return sorted(artifacts, key=lambda x: x['power'])


print("Sorted by power:")
display(artifact_sorter(artifacts=artifacts))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Let's filter"""
    return list(filter(lambda x: x['power'] >= min_power, mages))


min_power: int = 60
print(f"\nMages with min power {min_power}:")
display(power_filter(mages=mages, min_power=min_power))


def spell_transformer(spells: list[str]) -> list[str]:
    """Let's transform"""
    return list(map(lambda x: "* " + x + " *", spells))


print("\nWe added prefixes and sufixes")
display(spell_transformer(spells=spells))


def mage_stats(mages: list[dict]) -> dict:
    """Stats"""
    min_power: dict = min(mages, key=lambda x: x['power'])
    max_power: dict = max(mages, key=lambda x: x['power'])
    power_sum: int = sum(map(lambda x: x['power'], mages))

    average_power = power_sum / len(mages)

    return {
        "max_power": max_power['power'],
        "min_power": min_power['power'],
        "average": average_power
    }


print("\nOur stats:")
print(mage_stats(mages=mages))

print("\nThe end!")
