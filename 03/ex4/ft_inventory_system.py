#!/usr/bin/env python3
import sys


class InventoryError(Exception):
    def __init__(self, message="Inventory system") -> None:
        self.message = message


def main() -> None:
    print("=== Inventory System Analysis ===")

    try:
        if len(sys.argv) == 1:
            raise InventoryError("No arguments provided!")

        provided_items: list[str] = sys.argv[1:]
        inventory: dict[str, int] = {}
        total_items: int = 0

        for item_str in provided_items:
            if ":" not in item_str:
                raise InventoryError("Wrong format, lack of ':'")

            name, qty_str = item_str.split(":", 1)

            inventory[name] = int(qty_str)
            total_items += int(qty_str)

        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {len(inventory)}")

        print(inventory)
        print("\n=== Current Inventory ===")
        for name, quantity in inventory.items():
            precent = (quantity / total_items) * 100
            print(f"{name}: {quantity} units ({precent:.1f})%")

        print("\n=== Item Categories ===")
        moderate: dict[str, int] = {}
        scarce: dict[str, int] = {}
        for name, quantity in inventory.items():
            if name == "potion":
                moderate[name] = quantity
            else:
                scarce[name] = quantity

        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {', '.join(inventory.keys())}")

        values_str: list[str] = [str(v) for v in inventory.values()]
        print(f"Dictionary values: {', '.join(values_str)}")

        item_to_find: str = "sword"
        is_present = item_to_find in inventory
        print(f"Sample lookup - '{item_to_find}' in inventory: {is_present}")

    except InventoryError as e:
        print(f"InventoryError: {e}")


if __name__ == "__main__":
    main()
