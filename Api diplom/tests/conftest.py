import pytest
from methods.login_user import LoginUser
from data import USER

@pytest.fixture
def user_token():
    response = LoginUser.login_user(USER["email"], USER["password"])
    return response.json()["accessToken"]