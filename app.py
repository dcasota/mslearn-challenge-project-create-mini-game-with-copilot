# rock,scissors, paper
# weblink source 1 : https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list
# weblink source 2 : https://bobbyhadz.com/blog/python-select-option-input
# weblink source 3 : https://stackoverflow.com/questions/28425204/python-how-to-use-list-as-source-of-selection-for-user-input

import random
import inquirer # pip install inquirer

list = ["rock", "scissors", "paper"]

questions = [
  inquirer.List('choice',
                message="Make a choice ",
                choices=[list[0], list[1], list[2]],
            ),
]
answers = inquirer.prompt(questions)

P1 = answers['choice']
print ("You have chosen ",P1)

P2 = random.choice(list)
print ("Player 2 has chosen ",P2)

if P1 == P2:
    print ("No one wins.")
elif P1 == 'rock' and P2 == 'scissors':
    print ("You win!")
elif P1 == 'scissors' and P2 == 'paper':
    print ("You win!")
elif P1 == 'paper' and P2 == 'rock':
    print ("You win!")    
else: print ("You loose.")