print("Please type in integer numbers. Type in 0 to finish.")
count = 0
the_sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
    print(f"Numbers typed in {count}")
    the_sum += number
    print(f"The sum of the numbers is {the_sum}")
    mean = the_sum / count
    print(f"The mean of the numbers is {mean}")
    if number > 0:
        positive += 1
    else:
        negative += 1
    print(f"Positive numbers {positive}")
    print(f"Negative numbers {negative}")