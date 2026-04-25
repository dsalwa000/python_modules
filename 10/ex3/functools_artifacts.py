from typing import Callable, Any
from functools import reduce, lru_cache
from operator import add, mul
from enum import Enum
from functools import partial, singledispatch


class OperationType(Enum):
    ADD = "add"
    MULTIPLY = "multiply"
    MAX = "max"
    MIN = "min"


class OperationError(Exception):
    pass


"""Reducer"""


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise OperationError("Operation is unknown")

    final_operation = operations[operation]

    return reduce(lambda x, y: final_operation(x, y), spells)


spells: list[int] = [1, 3, 5, 6, 9]

"""
Using OperationType Enum you can pick easily type of operation

"""
try:
    operation_to_use = OperationType.ADD.value

    print(f"Let's try use operation '{operation_to_use}':")

    reducer_result = spell_reducer(
        spells=spells,
        operation=operation_to_use
    )
    print(f"Result: {reducer_result}")

except OperationError as e:
    print(e)

"""Partial"""


def cast_enchantment(power: int, element: str, target: str) -> str:
    return f"Casting {element} (Level {power}) on {target}!"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    enchanters: dict = {
        "fire": partial(base_enchantment, power=50, element="Fire"),
        "ice": partial(base_enchantment, power=50, element="Ice"),
        "lightning": partial(base_enchantment, power=50, element="Lightning"),
    }

    return enchanters


print("\nEnchanter usage:")
enchanters = partial_enchanter(cast_enchantment)

fire = enchanters["fire"]
ice = enchanters["ice"]
lightning = enchanters["lightning"]

print(fire(target="Dragon"))
print(ice(target="Wawrzyszew"))
print(lightning(target="Somewhere"))

"""lru_cache"""


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a positive integer!")
    if n <= 1:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


print("\nFibonacci numbers")
tenth_fib_number = memoized_fibonacci(10)
print(f"10th number: {tenth_fib_number}")

twentieth_fib_number = memoized_fibonacci(20)
print(f"20th number: {twentieth_fib_number}")

"""singledispatch"""


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast_spell(spell: Any) -> str:
        """Default case"""
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(damage: int) -> str:
        return f"Damage spell: {damage} damage"

    @cast_spell.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment: {enchantment}"

    @cast_spell.register(list)
    def _(spells: list[str]) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return cast_spell


print("\nDispatcher")
our_dispatcher = spell_dispatcher()

print(our_dispatcher(5.5))
print(our_dispatcher("Fireball"))
print(our_dispatcher(["SpellOne", "SpellTwo"]))
print(our_dispatcher({"bad": "type"}))
