import requests
import allure
from curl import URL


class LoginUser:
    @allure.step("Залогиниться юзером")
    def login_user(email, password):
        payload = {"email": email, "password": password}
        return requests.post(URL.LOGIN_USER, json=payload)
