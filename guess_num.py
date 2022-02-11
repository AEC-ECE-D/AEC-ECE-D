import random
s_guess=random.randint(1,10)
u_guess=int(input("enter the number::"))
if s_guess==u_guess:
    print("Yes,your guess number is correct")
else:
    print("No,your guess number is not correct")
