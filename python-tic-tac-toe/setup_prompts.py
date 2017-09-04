class SetupChoices():
    usr_letter_choice = ' '
    comp_letter_choice = ' '

def get_user_input(text):
    return input(text)

def user_choice():
    response = get_user_input('Player 1, please choose X or O')
    response.upper()
    if response == 'X':
        usr_letter_choice = 'X'
        comp_letter_choice = 'O'
        return 'X'
    if response == 'O':
        usr_letter_choice = 'O'
        comp_letter_choice = 'X'
        return 'O'
    else:
        print('That is not a valid character please select X or O')
        user_choice()

if __name__ == "__main__":
    user_letter_choice()
