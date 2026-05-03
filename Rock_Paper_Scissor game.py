"""
WORK FLOW OF PROJECT:
1. User gives input from (Rock, Paper, Scissors)
2. Computer choose(using random function)
3. Print Result

Cases:
A - Rock 
Rock - Rock = Tie
Rock - Paper = Paper wins
Rock - Scissor = Rock wins

B - Paper
Paper - Rock = Paper wins 
Paper - Paper = Tie
Paper - Scissor = Scissor wins 

C - Scissor
Scissor - Rock = Rock wins
Scissor - Paper = Scissor wins
Scissor - Scissor = Tie 


"""

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your choice = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: MATCH IS TIE!")

#IF CHOICE IS ROCK 

elif user_choice == "Rock":
    if comp_choice == "paper":
        print("Paper covers rock = COMPUTER WINS!")

    else:
        print("Rock smashes scissor: YOU WINS!")

#IF CHOICE IS PAPER

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts the paper = COMPUTER WINS!")
    else:
        print("Paper cover rock: YOU WIN!")

# IF CHOICE IS SCISSOR

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes the scissor = COMPUTER WINS!")
    else:
        print("Scissor cuts the paper = YOU WINS!")
