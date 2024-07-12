name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")
else:
    soup_portions = int(input("How many portions of soup? "))
    total_cost = soup_portions * 5.90
    print(f"The total cost is {total_cost}")
    print("Next please!")