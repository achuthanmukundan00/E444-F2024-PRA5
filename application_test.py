import requests

url = "http://ece444-pra5-app-environment.eba-3c2rf3gh.us-east-2.elasticbeanstalk.com/predict"

test_cases = [
    {"text": "This is a fake news article."},
    {"text": "Another fake news example."},
    {"text": "This is real news."},
    {"text": "This is an example of real news."}
]

for i, test_case in enumerate(test_cases):
    response = requests.post(url, json=test_case)

    print(f"Input: {test_case}")
    print(f"Raw Response (Test case {i + 1}): {response.text}")

    try:
        json_response = response.json()
        print(f"Prediction: {json_response['prediction']}\n")
    except ValueError as e:
        print(f"Failed to decode JSON: {e}")
        print(f"Response content: {response.content}")
