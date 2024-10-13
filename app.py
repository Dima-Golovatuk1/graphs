import pandas as pd
import matplotlib.pyplot as plt

file_path = 'csv/sell_data.csv'
data = pd.read_csv(file_path)

mean = data.iloc[:, 1:].mean(axis=1)
max = data.iloc[:, 1:].max(axis=1)
min = data.iloc[:, 1:].min(axis=1)

months = data['Month']

plt.figure(figsize=(10, 6))
plt.plot(months, mean, label='Mean', marker='o', color='blue')
plt.plot(months, max, label='Max', marker='^', color='green')
plt.plot(months, min, label='Min', marker='s', color='red')

plt.title('Monthly Sales Statistics for Products')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.tight_layout()
plt.show()
