class setupChoices():
    usr_letter_choice = ' '
    comp_letter_choice = ' '

def user_letter_choice(val):
    setupChoices.usr_letter_choice = val

def comp_letter_choice(val):
    setupChoices.comp_letter_choice = val

def who_goes_first(choice):
    if choice == 1:
        return "Player One: " + setupChoices.usr_letter_choice + " goes first"
    
