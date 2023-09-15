
import random

difficulty = str (input("pick a diffculty easy or hard ").lower())

if(difficulty=="hard"):
    Number_of_attempts=5
else:
    Number_of_attempts = 10

def guess_number(no_of_attempts):
    choice = random.randint(1,100)
    print("Choice -" + str(choice))
    while no_of_attempts>0:
        guess_num =  int(input("Pick a number between 1 to 100"))
        if(choice == guess_num):
            print("Congratulations, You guessed it correctly.")
            break
        elif(choice> guess_num):
            print("Your guess is too low")
            no_of_attempts-=1
        elif (choice< guess_num):
            no_of_attempts-=1
            print("Your guess is too high")
        if(no_of_attempts == 0):
            print("You lost")
        else:
            print(f"You only have {no_of_attempts} left")
guess_number(Number_of_attempts)