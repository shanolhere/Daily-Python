# Rock, Paper and Scissors Game with Python

import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
player_score = 0
cpu_score = 0
while True:
    player = input("Enter your choice: ").capitalize()
    #conditions
    if player == computer:
        print("Tie")
    elif player=="Rock":
        if computer == "Paper":
            print("You lose "+ computer +" covers "+ player)
            cpu_score+=1
        else:
            print("You win " + player + " smashes " +computer)
            player_score+=1 
    elif player == "Paper":
        if computer =="Scissors":
            print("You lose "+ computer +" cuts "+ player)
            cpu_score+=1
        else:
            print("You win " + player + " covers " +computer)
            player_score+=1  
    elif player == "Scissors":
        if computer =="Rock":
            print("You lose "+ computer +" smashes "+ player)
            cpu_score+=1
        else:
            print("You win " + player + " cuts " +computer)
            player_score+=1  
    elif player=="End":
        print('Final Scores')
        print('------------------------')
        print("player Score: "+str(player_score))
        print("Computer Score: "+str(cpu_score))
        break
        