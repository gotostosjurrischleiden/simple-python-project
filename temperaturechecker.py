# Temperature Checker Program

temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("Freezing temperature ❄️")
elif temperature <= 25:
    print("Normal temperature 🙂")
else:
    print("Hot temperature 🔥")