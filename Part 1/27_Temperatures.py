temperature_fahrenheit = int(input("Please type in the temperature (F): "))

celsius = (temperature_fahrenheit - 32) * 5 / 9

if celsius < 0:
    print(f"{temperature_fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{temperature_fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
