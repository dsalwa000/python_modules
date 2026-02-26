def test_temperature_input(temp_str: str):
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
        return

    print(f"Testing temperature: {temp_int}")
    if 0 <= temp_int <= 40:
        print(f"Temperature {temp_int}°C is perfect for plants!")
    elif temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants(min 0)")
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
