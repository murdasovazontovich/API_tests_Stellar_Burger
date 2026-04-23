import pytest
import allure
from data import LOGIN_USER
from data import INVALID_LOGIN_DATA 
from methods.login_user import LoginUser


class TestLoginUser:
    @allure.title("Залогиниться юзеру")
    def test_login_with_existing_user_returns_ok(self):
        response = LoginUser.login_user(LOGIN_USER["email"], LOGIN_USER["password"])
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "accessToken" in body
        assert "refreshToken" in body


    @allure.title("Неудачный залогин с неверным логином и паролем")
    @pytest.mark.parametrize("email, password", INVALID_LOGIN_DATA)
    def test_login_with_invalid_credentials_returns_401(self, email, password):
        response = LoginUser.login_user(email, password)
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "email or password are incorrect"