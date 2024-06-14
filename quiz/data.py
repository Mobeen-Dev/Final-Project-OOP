import requests

parameters = {
    "amount": 20,
    "type": "boolean",

    "difficulty": "medium"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
# https://opentdb.com/api.php?amount=15&category=18&difficulty=medium&type=boolean
