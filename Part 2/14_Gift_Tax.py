value_of_gift = int(input("Value of gift: "))

if value_of_gift > 1000000:
    print(f"Amount of tax: {(142100+(value_of_gift - 1000000) * 0.17)}")
elif value_of_gift <= 1000000 and value_of_gift >= 200000:
    print(f"Amount of tax: {(22100+(value_of_gift - 200000) * 0.15)} euros")
elif value_of_gift <= 200000 and value_of_gift >= 55000:
    print(f"Amount of tax: {(4700+(value_of_gift - 55000)* 0.12)} euros")
elif value_of_gift <= 55000 and value_of_gift >= 25000:
    print(f"Amount of tax: {(1700+(value_of_gift - 25000)* 0.10)} euros")
elif value_of_gift <= 25000 and value_of_gift >= 5000:
    print(f"Amount of tax: {(100+(value_of_gift - 5000)* 0.08)} euros")
else:
    print("No tax!")