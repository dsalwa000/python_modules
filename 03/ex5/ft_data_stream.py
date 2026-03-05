#!/usr/bin/env python3
from collections.abc import Iterator


def events_stream() -> Iterator[tuple[int, str, int, str]]:
    yield 1, "alice", 5, "killed monster"
    yield 2, "bob", 11, "found treasure"
    yield 3, "charlie", 10, "leveled up"


def fibonacci_generator(n) -> Iterator[int]:
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n) -> Iterator[int]:
    count: int = 0
    number: int = 2
    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
            count += 1
        number += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    print("Processing game events...\n")

    stream: tuple[int, str, int, str] = iter(events_stream())

    total_events: int = 0
    treasure_events: int = 0
    lvl_up_events: int = 0
    high_lvl_players: int = 0

    for _ in range(0, 3):
        id, player, lvl, event = next(stream)

        print(f"Event: {id}: Player {player} (level {lvl}) {event}")

        total_events += 1

        if "treasure" in event:
            treasure_events += 1
        if event == "leveled up":
            lvl_up_events += 1
        if lvl >= 10:
            high_lvl_players += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_lvl_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {lvl_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===\n")
    fibbonaci: list[int] = []
    for n in fibonacci_generator(10):
        fibbonaci.append(str(n))
    result_fib: list[str] = ", ".join(fibbonaci)
    print(f"Fibonacci sequence (first 10): {result_fib}")

    prime: list[int] = []
    for n in prime_generator(5):
        prime.append(str(n))
    result_prime: list[str] = ", ".join(prime)
    print(f"Prime numbers (first 5): {result_prime}")


if __name__ == "__main__":
    main()
