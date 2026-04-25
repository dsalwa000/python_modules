from typing import Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


next_call: Callable = mage_counter()

print("Let's count!")
for i in range(5):
    print(next_call())


def spell_accumulator(initial_power: int) -> Callable:
    power_accumulator: int = initial_power

    def accumulator(power: int):
        nonlocal power_accumulator
        power_accumulator += power
        return power_accumulator

    return accumulator


our_accumulator: Callable = spell_accumulator(20)

print("\nLet's accumulate power!")
for i in range(5):
    print(our_accumulator(i))


def enchantment_factory(enchantment_type: str) -> Callable:
    start_value: str = enchantment_type

    def add_something(enrichment: str):
        nonlocal start_value
        start_value += " " + enrichment
        return start_value

    return add_something


enrichment: Callable = enchantment_factory("Sword")

enrichments: list[str] = ["Good", "Better", "The Best"]

print("\nLet's enrich!")
for i in range(3):
    print(enrichment(enrichments[i]))


def memory_vault() -> dict[str, Callable]:
    storage: dict[str, int | str] = {}

    def store(key: str, value: int | str) -> None:
        storage[key] = value

    def recall(key: str) -> int | str:
        return storage.get(key, "Not found")

    return {"store": store, "recall": recall}


print("\nThe Vault")
vault = memory_vault()

print("Loading things to vault...")
vault['store']("login", "dsalwa")
vault['store']("password", 12345)

print("Recalling things from vault:")
print(vault['recall']("login"))
print(vault['recall']("password"))
print(vault['recall']("something"))
