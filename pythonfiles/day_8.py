import random

i = 0
random_num = str(random.randint(0, 9))

count = 0
guess = 10



another = None   

while True:

    count += 1
    print(f"you have remaining {guess} times")
    user = input("enter a number :")

    if user == random_num:
        print(f"successfully guessed number in {count} times\n")
        break   

    elif user != random_num:
        guess -= 1

    if guess == 0:
        another = input("do you want to play again (y/n)\n")

        if another != 'n':
            count = 0
            guess = 10  
            random_num = str(random.randint(0, 9))  
            continue
        else:
            print("try again")
            break