def recursive(my_range):
    if my_range == 6:
        print("Harvest time!")
        return
    print("Day", my_range)
    recursive(my_range + 1)


def ft_count_harvest_recursive():
    print("Days until harvest: 5")
    recursive(1)
