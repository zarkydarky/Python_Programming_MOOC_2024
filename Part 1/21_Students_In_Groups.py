amount_of_students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))

groups_formed = amount_of_students // desired_group_size

if amount_of_students % desired_group_size != 0:
    groups_formed += 1

print(f"Number of groups formed: {groups_formed}")