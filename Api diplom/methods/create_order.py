import requests
import allure
from curl import URL


class CreateOrder:
    @allure.step("Сделать заказ")
    def create_order(payload, token=None):
        headers = {}
        if token:
            headers = {"Authorization": token}
        return requests.post(URL.CREATE_ORDER, json=payload, headers=headers)