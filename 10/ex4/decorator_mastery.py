import time
import functools
from typing import Callable, Any

"""The time"""


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper() -> str:
        print(f"Casting {func.__name__}...")

        start_time = time.perf_counter()

        result = func()

        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} second\n")

        return result

    return wrapper


@spell_timer
def fireball():
    print("Inside fireball")
    time.sleep(1)
    return "Fireball cast!"


print("Testing spell timer...\n")
output = fireball()
print(f"Result: {output}")

"""The validator"""


def power_validator(min_power: int) -> Callable:
    """This function allows us to provide arguments to a decorator"""

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> Any:
            if power >= min_power:
                return func(power, *args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


@power_validator(min_power=50)
def lightning(power: int, target: str):
    return f"McQueen attacked {target} with {power} power"


print("\nParameterized validation decorator")
print(lightning(60, "Someone"))
print(lightning(40, "SomeoneTwo"))

"""Retry spell"""


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


@retry_spell(max_attempts=5)
def download_spell(what: str) -> str:
    """Uncomment this to test download_spell with failing"""
    # import random
    # if random.random() < 0.7:
    #     raise Exception("Mana unstable!")
    return f"We downloaded {what}!"


print("\nRetry:")
print(download_spell("Movie"))

"""MageGuild"""


def validate_mage_power(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(self, power: int, *args: Any, **kwargs: Any) -> str:
            if power >= min_power:
                return func(self, power, *args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        return name.replace(" ", "").isalpha()

    @validate_mage_power(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


print("\nLet's test MageGuild")
guild = MageGuild()

name_one = "Gandalf"
name_bad = "N2"

print(f"Is {name_one} cool: {MageGuild.validate_mage_name(name_one)}")
print(f"Is {name_bad} cool: {MageGuild.validate_mage_name(name_bad)}")

print()

print(guild.cast_spell(13242412, "Weak Skills"))
print(guild.cast_spell(1, "Fireball"))
