import random

def generate_random_number():
    rand_num = random.randint(0,9)
    print("I have a single digit number. Guess the number?")
    return rand_num

while (True):
    print("Want to play 'Guess the number'? (y/n)")
    ans = input()

    if ans == "y":
        num = generate_random_number()
        status = True

        while(status):
            guess = int(input())

            if (guess >= 10):
                print("I said single digit number")

            elif (guess == num):
                print("WOW!! You got it right. The number is ", guess)
                status = False

            elif (guess < num):
                print("Your guess is lower than the number. Try again")

            else:
                print("Your guess is higher than the number. Try again")

    elif ans == "n":
        print("Why not?")

    else:
        print("Invalid Input")
