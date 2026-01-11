# Temperature Checker Program (Extended Version)

print("=== TEMPERATURE CHECKER ===")

# Ask the user for temperature input
user_input = input("Enter the temperature in Celsius: ")

# Check if the input is a number
if user_input.replace('.', '', 1).replace('-', '', 1).isdigit():

    temperature = float(user_input)

    print("\nTemperature entered:", temperature, "°C")

    # Temperature classification
    if temperature < 0:
        status = "Freezing temperature ❄️"
    elif temperature <= 25:
        status = "Normal temperature 🙂"
    elif temperature <= 35:
        status = "Warm temperature 🌤️"
    else:
        status = "Hot temperature 🔥"

    print("Status:", status)

    # Convert temperature to Fahrenheit and Kelvin
    fahrenheit = (temperature * 9 / 5) + 32
    kelvin = temperature + 273.15

    print("\nTemperature Conversions:")
    print("Fahrenheit:", round(fahrenheit, 2), "°F")
    print("Kelvin:", round(kelvin, 2), "K")

    # Extra message based on temperature
    if temperature < 0:
        print("\nAdvice: Wear thick clothes to stay warm.")
    elif temperature <= 25:
        print("\nAdvice: The weather is comfortable.")
    else:
        print("\nAdvice: Stay hydrated and avoid too much heat.")

else:
    print("\nInvalid input. Please enter a valid number.")

print("\n=== PROGRAM ENDED ===")