import pytest
from user_responses import a_user_response

def test_a_function_returns_hello_world():
    assert a_user_response() == 'Hello World'

