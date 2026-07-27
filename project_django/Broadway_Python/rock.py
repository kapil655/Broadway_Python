import random

choices = ['r', 's', 'p']

count = 5

while True:
    computer = random.choice(choices)   

    user = input("enter r, s, p: ").lower()

    #
    if user not in choices:
        count -= 1
        print(f"invalid choice! attempts left: {count} ")

        if count == 0:
            anothertime = input("do you want to play again (y/n): ").lower()

            if anothertime == 'y':
                count = 5  
                continue
            else:
                break

        continue   

    # computer wins
    if computer == 'r' and user == 's':
        print("computer wins")
        print(computer)
        break

    elif computer == 's' and user == 'p':
        print("computer wins")
        print(computer)
        break

    elif computer == 'p' and user == 'r':
        print("computer wins")
        print(computer)
        break

    # user wins
    elif user == 'r' and computer == 's':
        print("user wins")
        print(computer)
        break

    elif user == 'p' and computer == 'r':
        print("user wins")
        print(computer)
        break

    elif user == 's' and computer == 'p':
        print("user wins")
        print(computer)
        break

    elif user == computer:
        print("tie, try again")
        continue