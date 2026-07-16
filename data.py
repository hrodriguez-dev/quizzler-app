import requests

#API parameters required
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 27,
    "difficulty": "easy"
}

#Get the question data from the API - Use this website to config API -> https://opentdb.com/api_config.php
response = requests.get("https://opentdb.com/api.php", params=parameters )
response.raise_for_status()

question_data = response.json().get("results")