import pytest
import allure
from methods.create_user import CreateUser
from data import USER
from generators import generate_user_payload


class TestCreateUser:
    @allure.title("Создание ползователя без обязательного поля")
    @pytest.mark.parametrize("payload", [{"password": "12345"},
                                          {"name": "piojh"},])
    def test_create_user_missing_required_field(self,payload):
        response = CreateUser.create_user(payload=payload)
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"


    @allure.title("Создание ползователя")
    def test_create_user(self):
        payload = generate_user_payload()
        response = CreateUser.create_user(payload=payload)

        assert response.status_code == 200

    @allure.title("Создание ползователя, который существует")
    def test_create_already_exist_user(self):
        response = CreateUser.create_user(payload = USER)
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "User already exists"