from typing import Callable

"""
All data necessary to conduct our magic

"""
target: str = "JakisMaciek"
power: int = -20


def heal(target: str, power: int) -> str:
    return f"Heal restores {power} HP for {target}"


def attack(target: str, power: int) -> str:
    return f"Attack {target} takes {power} HP"


spells_list: list[Callable] = [heal, attack]


"""Our code starts"""


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Let's combine our spells"""

    def conbined_spell(target: str, power: int):
        print(spell1(target, power))
        print(spell2(target, power))

    return conbined_spell


print("Combine power axis:")
double_call: Callable = spell_combiner(heal, attack)
double_call(target, power)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Let's make our spell more powerfull"""

    def more_power(target: str, power: int):
        even_more_power: int = power * multiplier
        return base_spell(target, even_more_power)

    return more_power


print("\nMore power:")
respect_power_banana: Callable = power_amplifier(heal, 4)
print(respect_power_banana(target, power))


def our_condition() -> bool:
    """You can change it to False easily"""
    return True


def conditional_caster(condition: Callable, spell: Callable) -> Callable | str:
    """We have some conditions"""

    if condition():
        return spell

    return "Spell fizzled"


try:
    print("\nConditional:")
    yes_or_no: Callable | str = conditional_caster(our_condition, attack)

    if isinstance(yes_or_no, str):
        print(yes_or_no)
    else:
        print(yes_or_no(target, power))

except TypeError as e:
    print(e)


def spell_sequence(spells: list[Callable]) -> Callable:
    """We call everything"""

    def sequence(target: str, power: int):
        for spell in spells:
            print(spell(target, power))

    return sequence


print("\nCall everything:")
everything: Callable = spell_sequence(spells_list)
everything(target, power)
