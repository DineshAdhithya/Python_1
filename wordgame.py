import xlrd
import random

class Word():
    
    def rand_word(self):
        loc = ("E:\Python Practice\Words.xlsx") 
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0)
        rand_num = random.randint(0,25487)
        return(sheet.cell_value(rand_num, 0))
    
while True:
    print("Do you want to play \"Word game\"? (y/n)")
    status = str(input())

    if status == "y":
        word = Word()
        my_word = word.rand_word()
        #my_word = "apple"
        temp_word = my_word
        length = len(my_word)
        remain_length = length
        print("The word contains ", length, "letters")
        print("Guess the word or guess any one letter")
        answer = "Wrong"

        while (answer == "Wrong"):
            guess = str(input())

            if len(guess) == 1:

                if guess in temp_word:
                    print("This letter is in the word")

                    for position in range(length):
                        
                        if my_word[position] == guess:
                            print("In position ", position+1)
                            temp_word = temp_word.replace(guess,"")
                            remain_length -= 1

                    if remain_length == 0:
                        print("You got all the letters")
                else:
                    print("Wrong letter / Don't repeat")

            elif len(guess) == length:

                if guess == my_word:
                    print("WOW! You got it. The word is ", my_word)
                    print("Your score is ", remain_length+length, "/", 2*length)
                    answer = "Correct"

            elif len(guess) > 0:
                print("Try again one letter at time")

            else:
                print("Wrong word. Try again")

    elif status == "n":
        print("I won't take no for an answer")

    else:
        print("Invalid comment")


        
                
