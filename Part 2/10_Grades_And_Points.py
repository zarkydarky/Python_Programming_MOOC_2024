points = int(input("How many points [0-100]: "))

if points > 100:
    print("Grade: impossible!")
elif points <= 100 and points >= 90:
    print("Grade: 5")
elif points <= 89 and points >= 80:
    print("Grade: 4")
elif points <= 79 and points >= 70:
    print("Grade: 3")
elif points <= 69 and points >= 60:
    print("Grade: 2")
elif points <= 59 and points >= 50:
    print("Grade: 1")
elif points <= 49 and points >= 0:
    print("Grade: fail")
else:
    print("Grade: impossible!")