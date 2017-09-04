class SetupChoices():
    who_goes_first = ' '
    usr_letter_choice = ' '
    comp_letter_choice = ' '

def get_user_input(text):
    return input(text)

def user_choice():
    response = get_user_input('Player 1, please choose X or O: ')
    response.upper()
    if response == 'X':
        print('Player 1, your letter is X')
        print('Player 2, your letter is O')
        usr_letter_choice = 'X'
        comp_letter_choice = 'O'
        return 'X'
    if response == 'O':
        print('Player 1, your letter is O')
        print('Player 2, your letter is X')
        usr_letter_choice = 'O'
        comp_letter_choice = 'X'
        return 'O'
    else:
        print('That is not a valid character please select X or O')
        user_choice()

def who_goes_first():
    response = get_user_input("Please choose who should go first? 1. Player 1  2. Player 2 : ")
    response = int(response)
    if response == 1:
        print("Player 1 has the first move")
        SetupChoices.who_goes_first = SetupChoices.usr_letter_choice 
        return 1
    if response == 2:
        SetupChoices.who_goes_first = SetupChoices.comp_letter_choice
        print("Player 2 has the first move")
        return 2
    else: 
        print("That is not a valid choice, please select 1 or 2")
        who_goes_first()

def game_mode_selection():
    response = get_user_input("Please choose a game mode: 1. Player V Player 2. Player V Computer 3. Computer V Computer  ")
    response = int(response)
    if response == 1:
        print("You have chosen Player V Player")
        SetupChoices.game_mode_selection = "Player V Player"
        return "Player V Player"   
    elif response == 2:
        print("You have chosen Player V Computer")
        SetupChoices.game_mode_selection = "Player V Computer"
        return "Player V Computer"
    elif response == 3:
        print("You have chosen Computer V Computer")
        SetupChoices.game_mode_selection = "Computer V Computer"
        return "Computer V Computer"
    else: 
        print("That is not a valid choice. Choose: 1. Player V Player 2. Player V Computer 3. Computer V Computer")
        game_mode_selection()

if __name__ == "__main__":
    user_choice()
    who_goes_first()
    game_mode_selection()
