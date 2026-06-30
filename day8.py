import random
i=0
random_num=str(random.randint(0,9))

count=0
guess=2

count=0
while True:

    
    count+=1
    print(f"you have remaining {guess} times")
    user=input("enter a number :")
    if user == random_num:
        print(f"successfully guessed number in {count} times")     
        break

    elif user != random_num:
        guess-=1
    if guess == 0:
        break
            
    else:
        print("try again")



        

    


