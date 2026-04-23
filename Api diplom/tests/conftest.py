import pytest
from methods.delete_user import DeleteUser
import pytest
from generators import generate_user_payload
from methods.create_user import CreateUser
from methods.delete_user import DeleteUser


@pytest.fixture
def cleanup_user():
    user_data = {}

    yield user_data

    access_token = user_data.get("access_token")
    if access_token:
        DeleteUser.delete_user(access_token)

@pytest.fixture
def user_token():
    payload = generate_user_payload()
    response = CreateUser.create_user(payload=payload)
    access_token = response.json()["accessToken"]

    yield access_token

    DeleteUser.delete_user(access_token)
