
import requests

parameters = {
    "amount": 20,
    "type": "boolean",
    "category": 27,  # 18
    # "difficulty": "easy"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# print(response.json()["results"])

question_data = response.json()["results"]

