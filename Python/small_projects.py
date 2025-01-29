# (1) Stone, Paper, Scissor game:

# s   1   stone
# w  -1   scissor
# g   0   paper

dict={"stone":1, "scissor":-1, "paper":0}

import random

options = ["stone", "scissor", "paper"]
computer = random.choice(options)
comp = dict[computer]

user=(input("Choose any one of them (Stone, Paper, Scissor) : ")).lower()
your=dict[user]

score=0

if your==comp:
    print("It's a Draw")
else:
    if your==1 and comp==-1:
        print("hey, You won the Game")
        score+=1
    elif your==1 and comp==0:
        print("You Loose the Game, Try again")            
    elif your==0 and comp==1:
        print("hey, You won the Game") 
        score+=1           
    elif your==0 and comp==-1:
        print("You Loose the Game, Try again")            
    elif your==-1 and comp==0:
        print("hey, You won the Game")  
        score+=1          
    elif your==-1 and comp==1:
        print("You Loose the Game, Try again")  

print(f"The Options were selected by you and the Computer are {user} and {computer} respectively")

#  (2) The game() function in a program lets a user play a game and returns the score as an integer. You need to read a
#  file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to 
#  update the Hiscore whenever the game() function breaks the Hi-score.

import random
def game():

    print("We will update your highest score :")

    score=random.randint(1,10)

    with open("game.txt","r") as f:
        highscore=f.read()
        if highscore=="":
            highscore=0
        else:
            highscore=int(highscore)  
        
        print(f"your score is {score} and the highscore is {highscore}")

        if (score>highscore):
            with open("game.txt","w") as f:
                f.write(str(score))

game()

# (3) We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher number please” 
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.   

import random

comp = random.randint(1, 100) 
user = -1  
count = 0  

while comp != user:
    try:
        user_input = input("Guess the number from 1 to 100: ")
        
        if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
            print(f"Program ended. The correct number was {comp}")
            break
        
        user = int(user_input)  
        count += 1  

        if user < 0: 
            print("Please enter a valid number (1-100). Negative numbers are not allowed.")
            continue
        
        if user > comp:
            print("Lower number please")
        elif user < comp:
            print("Higher number please")
        else:  # If the guess is correct
            print(f"Correct! The number was {comp}. You took {count} guesses.")
    
    except ValueError:
        print(f"Program ended. The correct number was {comp}")
        break


