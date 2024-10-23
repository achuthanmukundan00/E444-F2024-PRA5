import requests

# Define the API endpoint (replace with your AWS Elastic Beanstalk URL)
url = "http://ece444-pra5-app-environment.eba-3c2rf3gh.us-east-2.elasticbeanstalk.com/predict"

# Test cases: 2 fake news, 2 real news
test_cases = [
    {"text": "This is a fake news article."},
    {"text": "Another fake news example."},
    {"text": "This is a real news article."},
    {"text": "This is an example of real news."}
]

# Run the functional tests
for i, test_case in enumerate(test_cases):
    response = requests.post(url, json=test_case)

    # Print the raw response content
    print(f"Raw Response (Test case {i + 1}): {response.text}")

    # Check if the response was valid JSON before trying to decode
    try:
        json_response = response.json()
        print(f"Prediction: {json_response['prediction']}\n")
    except ValueError as e:
        print(f"Failed to decode JSON: {e}")
        print(f"Response content: {response.content}")
