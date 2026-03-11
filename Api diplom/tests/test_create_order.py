import allure
from methods.create_order import CreateOrder
from data import ORDER

class TestCreateOrder:
    @allure.title("Создание заказа c аторизацией и ингредиентами")
    def test_create_order_with_auth_and_ingredients_returns_success(self, user_token):
        response = CreateOrder.create_order(payload=ORDER, token=user_token)
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "name" in body
        assert "order" in body


    @allure.title("Создание заказа без авторизации и ингредиентами")
    def test_create_order_without_auth_returns_error(self):
        response = CreateOrder.create_order(payload=ORDER)
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False

    @allure.title("Создание заказа с авторизацией и без ингредиентов")
    def test_create_order_without_ingredients_returns_400(self, user_token):
        payload = {"ingredients": []}
        response = CreateOrder.create_order(payload=payload, token=user_token)
        body = response.json()

        assert response.status_code == 400
        assert body["success"] is False
        assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с авторизацией и неправильным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash_returns_500(self, user_token):
        playload = {"ingredients": ["61c0c5"]}
        response = CreateOrder.create_order(payload=playload, token=user_token)

        assert response.status_code == 500