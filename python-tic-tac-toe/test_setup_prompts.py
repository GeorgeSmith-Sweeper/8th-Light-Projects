import pytest
from setup_prompts import user_letter_choice
from setup_prompts import comp_letter_choice
from setup_prompts import who_goes_first
from setup_prompts import setupChoices 

def test_user_letter_choice_returns_selected_letter():
    user_letter_choice('X')
    assert setupChoices.usr_letter_choice == 'X'

def test_comp_letter_choice_returns_selected_letter():
    comp_letter_choice('O')
    assert setupChoices.comp_letter_choice == 'O'
    
def test_who_goes_first_replies_with_computer():
    assert who_goes_first(1) == 'Player One: ' + setupChoices.usr_letter_choice + ' goes first'
