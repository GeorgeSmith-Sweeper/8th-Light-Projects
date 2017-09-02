import pytest
from setup_prompts import user_letter_choice
from setup_prompts import setupChoices 

def test_user_letter_choice_returns_selected_letter():
    user_letter_choice()
    assert setupChoices.usr_letter_choice == 'X'

