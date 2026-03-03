import math


def distance_3d(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(str_coordinates: str):
    coordinates: list[int] = []
    for coordinate in str_coordinates.split(","):
        coordinates.append(int(coordinate))

    return (coordinates[0], coordinates[1], coordinates[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    position_zero = (0, 0, 0)

    position = (10, 20, 5)
    print(f"\nPosition created: {position}")
    print(f"Distance between {position_zero} and {position}: "
          f"{distance_3d(position_zero, position):.2f}")

    str_position = "3,4,0"
    print(f"\nParsing coordinates: {str_position}")
    parsed_coordinates = parse_coordinates(str_position)

    print(f"Parsed position: {parsed_coordinates}")
    print(f"Distance between {position_zero} and {parsed_coordinates}: "
          f"{distance_3d(position_zero, parsed_coordinates):.2f}")

    try:
        wrong_position = "abc,def,ghi"
        print(f"\nParsing coordinates: {wrong_position}")
        parsed_coordinates = parse_coordinates(wrong_position)

        print(f"Parsed position: {parsed_coordinates}")
        print(f"Distance between {position_zero} and {position}: "
              f"{distance_3d(position_zero, position):.2f}")
    except ValueError as e:
        print(f"ValueError: {e}")

    print("\nUnpacking demonstration:")
    x, y, z = parsed_coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
