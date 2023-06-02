import random
import sys
user_choice = input("Rock, Paper, Scissors: ")
choices = {
    'Rock':{'beats':'Scissors'},
    'Paper':{'beats':'Rock'},
    'Scissors':{'beats':'Paper'}
}
computer_choice=random.choice(list(choices.keys()))
if user_choice not in choices:
    print("Invalid Input")
    sys.exit()
    # if not exit result still print
else:
    pass
    #underrated function
if user_choice == computer_choice:
    print("Tie")
elif choices[user_choice]['beats'] == computer_choice:
    #key comparison
    print("Win")
else:
    print("Lost")
