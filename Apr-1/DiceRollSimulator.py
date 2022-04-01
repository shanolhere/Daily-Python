#Dice Roll Simulator with Python
import random
max_value = 6
min_value = 1 

play_again = "YES"

while play_again=="YES" or play_again=='y':
    print("Rolling Dices..")
    print("The values are: ")
    
    print(random.randint(min_value, max_value))
    print(random.randint(min_value, max_value))
    
    play_again = input("Do you want to play again? ")


'''
import random
import time

while True:
    dice_rolled = random.randint(1, 6)
    user = str(input(" 'C' for Continue or 'Q' for Quit : ").upper())
    if user == 'C':
        print('Dice rolling …')
        time.sleep(2)
        print(dice_rolled)
        print('—————————————-')
    else:
        break
'''