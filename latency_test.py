import requests
import csv
import time

url = "http://ece444-pra5-app-environment.eba-3c2rf3gh.us-east-2.elasticbeanstalk.com/predict"

test_cases = [
    {"text": "This is a fake news article."},
    {"text": "Another fake news example."},
    {"text": "This is real news."},
    {"text": "This is an example of real news."}
]

# Open a CSV file to write the timestamps
with open('latency_test_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Test Case', 'Request Number', 'Start Time', 'End Time', 'Latency (s)'])

    # Perform 100 API calls for each test case
    for i, test_case in enumerate(test_cases):
        for j in range(100):
            start_time = time.time()  # Record the start time
            response = requests.post(url, json=test_case)
            end_time = time.time()  # Record the end time

            # Calculate latency
            latency = end_time - start_time

            # Write to CSV
            writer.writerow([i + 1, j + 1, start_time, end_time, latency])

            # Print result to console (optional)
            print(f"Test Case {i + 1}, Request {j + 1}: Latency = {latency:.4f} seconds")
