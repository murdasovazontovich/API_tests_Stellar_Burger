from faker import Faker

fake = Faker()

def generate_user_payload():
    return {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.user_name()
    }