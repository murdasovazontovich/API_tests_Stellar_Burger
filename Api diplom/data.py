USER = {"email": "zontovich_39@yandex.ru",
           "password": "123456",
           "name": "Екатерина"}

LOGIN_USER = {"email": "zontovich_39@yandex.ru",
           "password": "123456"}

ORDER = {"ingredients": 
         ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa7a"]}

INVALID_LOGIN_DATA = [
    ("wrong@mail.com", "123456"),
    ("zontovich_39@yandex.ru", "wrong_password"),
    ("wrong@mail.com", "wrong_password"),]

USER_WITHOUT_REQUIRED_FIELDS = [
    {"password": "12345"},
    {"name": "piojh"},]