hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day_of_Week = input("Day of the week: ")



if day_of_Week == "Sunday":
    daily_wages = (hourly_wage * 2) * hours_worked
    print(f"Daily wages: {daily_wages} euros")
else:
    daily_wages = hourly_wage * hours_worked
    print(f"Daily wages: {daily_wages} euros")