eating = int(input("How many times a week do you eat at the student cafeteria? "))
price_of_lunch = float(input("The price of a typical student lunch? "))
money_on_groceries = float(input("How much money do you spend on groceries in a week? "))

weekly_expenditure = float(eating * price_of_lunch + money_on_groceries)
daily_expenditure = weekly_expenditure / 7

print()
print("Average food expenditure: ")
print(f"Daily: {daily_expenditure} euros")
print(f"Weekly: {weekly_expenditure} euros")