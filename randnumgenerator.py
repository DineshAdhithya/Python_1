import random

def generate_random_number(range_min, range_max):
    num = random.randint(range_min, range_max)
    print("Your random number is ", num)

while True:
    print("Do you want to generate a random number? (y/n)")
    answer = str(input())

    if answer == "y":
        print("Enter the range")
        min_num = int(input())
        max_num = int(input())
        generate_random_number(min_num, max_num)

    elif answer == "n":
        print("No number to show")

    else:
        print("Invalid Input")
