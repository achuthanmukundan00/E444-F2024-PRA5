import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('latency_test_results.csv')

# Create a boxplot for each test case's latency
df.boxplot(column='Latency (s)', by='Test Case', grid=False)

# Label the plot
plt.title('API Latency Boxplot for Each Test Case')
plt.suptitle('')  # Remove the automatic subtitle
plt.xlabel('Test Case')
plt.ylabel('Latency (seconds)')

# Show the plot
plt.show()
