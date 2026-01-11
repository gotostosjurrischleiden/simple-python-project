# Temperature Checker Program

# Ask user for temperature input in Celsius
temp = input("Enter temperature in Celsius: ")

# Check if input is a valid number
if temp.replace('.', '', 1).replace('-', '', 1).isdigit():
    temp = float(temp)  # Convert input to float
    print(f"\nTemperature: {temp}°C")  # Display entered temperature

    # Classify temperature and give advice
    if temp < 0:
        status, advice = "Freezing ❄️", "Wear warm clothes."
    elif temp <= 25:
        status, advice = "Normal 🙂", "Comfortable weather."
    elif temp <= 35:
        status, advice = "Warm 🌤️", "Stay cool."
    else:
        status, advice = "Hot 🔥", "Stay hydrated."

    print("Status:", status)  # Show temperature status
    # Convert Celsius to Fahrenheit and display
    print("Fahrenheit:", round((temp*9/5)+32, 2), "°F")
    # Convert Celsius to Kelvin and display
    print("Kelvin:", round(temp+273.15, 2), "K")
    print("Advice:", advice)  # Show advice based on temperature
else:
    print("Invalid input. Enter a number.")  # Handle invalid input
