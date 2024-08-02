from math import sqrt

while True:
    n1 = int(input("Please type in a number: "))
    if n1 > 0:
        print(f"{sqrt(n1)}")
    elif n1 < 0:
        print("Invalid number")
    else:
        print("Exiting...")
        break