import random

choices = ['r', 's', 'p']
computer = random.choice(choices)

count = 5


while True:
    user = input("enter r, s, p: ").lower()

    #
    if user not in choices:
        count -= 1
        print(f"invalid choice! attempts left: {count}")

        if count == 0:
            print("too many attempts")
            break
        

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