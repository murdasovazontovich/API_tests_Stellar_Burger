import requests
import allure
from curl import URL


class CreateUser:
    @allure.step("Создание  пользователя")
    def create_user(payload):
        return requests.post(URL.CREATE_USER, json=payload)
