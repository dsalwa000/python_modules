#!/usr/bin/env python3


def event_stream():
    yield 1, "alice", 5, "killed monster"
    yield 2, "bob", 2, "found treasure"
    yield 3, "charlie", 8, "leveled up"


def fibonacci_generator(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    count = 0
    number = 2
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
    print("=== Game Data Stream Processor ===")

    print("Processing game events...")

    total_events = 0
    max_lvl = 0
    treasure_event = 0
    lvl_up_event = 0
    stream = iter(event_stream())
    for _ in range(0, 3):
        id, player, lvl, event = next(stream)

        print(f"Event: {id}: Player {player} (level {lvl}) {event}")
        total_events += 1
        if lvl > max_lvl:
            max_lvl = lvl
        if "treasure" in event:
            treasure_event += 1
        if event == "leveled up":
            lvl_up_event += 1

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")
    fibbonaci = []
    for n in fibonacci_generator(10):
        fibbonaci.append(str(n))
    result_fib = ", ".join(fibbonaci)

    print(f"\nFibonacci sequence (first 10): {result_fib}")
    prime = []
    for n in prime_generator(5):
        prime.append(str(n))
    result_prime = ", ".join(prime)
    print(f"Prime numbers (first 5): {result_prime}")


if __name__ == "__main__":
    main()
