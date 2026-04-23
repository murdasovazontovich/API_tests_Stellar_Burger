import pytest
import allure
from methods.create_user import CreateUser
from data import USER_WITHOUT_REQUIRED_FIELDS
from generators import generate_user_payload


class TestCreateUser:
    @allure.title("Создание ползователя без обязательного поля")
    @pytest.mark.parametrize("payload", USER_WITHOUT_REQUIRED_FIELDS)
    def test_create_user_missing_required_field(self,payload):
        response = CreateUser.create_user(payload=payload)
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False
        assert body["message"] == "Email, password and name are required fields"


    @allure.title("Создание пользователя")
    def test_create_user(self, cleanup_user):
        payload = generate_user_payload()
        response = CreateUser.create_user(payload=payload)
        body = response.json()

        cleanup_user["access_token"] = body.get("accessToken")

        assert response.status_code == 200
        assert body["success"] is True

    @allure.title("Создание пользователя, который уже существует")
    def test_create_already_exist_user(self, cleanup_user):
        payload = generate_user_payload()

        first_response = CreateUser.create_user(payload=payload)
        first_body = first_response.json()
        cleanup_user["access_token"] = first_body.get("accessToken")

        second_response = CreateUser.create_user(payload=payload)
        second_body = second_response.json()

        assert second_response.status_code == 403
        assert second_body["success"] is False
        assert second_body["message"] == "User already exists"
