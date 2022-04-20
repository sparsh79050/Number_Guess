import random
computer_guess= random.randint(1,10)
limit, score= 0,0
while limit<3:
    try:
        user_guess= int(input("Guess a number between 1-10: "))
        if(user_guess> 10 or user_guess<0):
            print("Input range should be 1-10")
            continue

    except:
        print("Please give correct input")
        continue

    if(computer_guess == user_guess):
        if(limit==0): score+=15
        elif(limit==1): score+=10
        else: score+=5
        break

    elif(computer_guess > user_guess):
        print("Your Guess number is lower than my number ")

    else: print("Your Guess number is upper than my number ")
    limit+=1

if(limit>2):
    print("Oops, You tried many times!")
    print(f"My number was {computer_guess}")

else:
    print("Congrats, you Guessed the number!!!")
    print(f"Your score is {score}")