#!/usr/bin/env python3
from typing import Generator


def invoice_generator(beginnig: int) -> Generator[str, float, str]:
    number = beginnig
    vat = 0.23

    print(f"--- System start {beginnig} ---")

    while number < beginnig + 3:
        new_value = yield f"Faktura nr {number}/2024 (VAT: {vat*100}%)"

        if new_value is not None:
            vat = new_value
            print(f"-> Zmieniono stawkę VAT na: {vat*100}%")

        number += 1

    return "End of the report"


def main() -> None:
    print("=== Inventory System Analysis ===")

    gen = invoice_generator(101)

    print(next(gen))
    print(gen.send(0.08))


if __name__ == "__main__":
    main()
