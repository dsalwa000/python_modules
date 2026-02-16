def ft_seed_inventory(vegetable: str, quantity: int, type_of: str):
    vegetable_upper = vegetable[0].upper() + vegetable[1:]
    if (type_of == "packets"):
        print(vegetable_upper, "seeds:", quantity, type_of, "available")
    if (type_of == "grams"):
        print(vegetable_upper, "seeds:", quantity, type_of, "total")
    if (type_of == "area"):
        print(vegetable_upper, "seeds: covers", quantity, "square meters")
