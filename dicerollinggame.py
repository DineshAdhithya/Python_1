import random
import time

def rolling_dice():
    print("Rolling Dice")

    for temp in range(0,3):
        print(".")
        time.sleep(0.5)

    num = random.randint(1,6)
    print("You got a ", num)

while True:
    print("Do you want to roll the Dice? (y/n)")
    answer = str(input())

    if answer == "y":
        rolling_dice()

    elif answer == "n":
        print("No dice to roll")

    else:
        print("Invalid Input")
