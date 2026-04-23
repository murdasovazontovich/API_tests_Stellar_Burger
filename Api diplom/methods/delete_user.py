import requests
import allure
from curl import URL


class DeleteUser:
    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {"Authorization": token}
        return requests.delete(URL.DELETE_USER, headers=headers)