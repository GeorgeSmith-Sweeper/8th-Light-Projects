import sys, os

class setupChoices():
    usr_letter_choice = ' '
    comp_letter_choice = ' '

def user_letter_choice():
    response = input("Player 1, please select a letter")
    setupChoices.usr_letter_choice = response

    
if __name__ == "__main__":
    user_letter_choice()
