#Create a Quiz Game with Python
def check_guess(guess, answer):
    global score
    attempt = 0
    still_guessing = True
    
    while(still_guessing and attempt<3) :
        if guess.lower() == answer.lower():
            print("Your Guess is 100% correct ^-^")
            score+=1 
            still_guessing = False
        else:
            if attempt<2:
                guess = input("Sorry Wrong Answer, try again")
            attempt+=1 
    if attempt ==3:
        print("No attempts")
        print("The correct answer is: "+answer)
    
score = 0
print("Guess the Animal:")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+ str(score))