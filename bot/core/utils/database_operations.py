import requests
from core.config import API_URL


def is_user_exists(user_id):
    url = f"{API_URL}/users/user/{user_id}/"
    response = requests.get(url)
    data = response.json()
    print(data)
    return len(data) > 0