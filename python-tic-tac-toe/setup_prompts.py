class SetupChoices():
    usr_letter_choice = ' '
    comp_letter_choice = ' '

def get_user_input(text):
    return input(text)

def user_choice():
    response = get_user_input('choose X')
    response.upper()
    if response == 'X':
        return 'X'
    
if __name__ == "__main__":
    user_letter_choice()
