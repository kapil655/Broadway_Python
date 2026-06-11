import random

for i in range(1,9):
    
    user_input = input("enter an number :")

    rand_num = random.randint(0,8)

    if user_input == rand_num:

        print("random generated number is",rand_num)

        break

    print(rand_num)

else:
   
   print("try again")



#    import random

# for i in range(1, 7):
#     user_num = int(input("Enter a number (1-6): "))

   
#     rand_num = random.randint(1, 6)
#     print("Computer generated:", rand_num)

#     if user_num == rand_num:
#         print("Correct! You win 🎉")
#         break
#     else:
#         print("Wrong 😢 Try again")