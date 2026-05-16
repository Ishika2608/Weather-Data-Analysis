import pandas as pd

# Load the dataset
weather_data = pd.read_csv('weather_data.csv')

# Display first few rows of the dataset
print(weather_data.head())

# Display summary statistics
print(weather_data.describe())

# Check for missing values
print(weather_data.isnull().sum())

# Check the data types
print(weather_data.dtypes)

# Convert the Date column to datetime
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Verify the conversion
print(weather_data.dtypes)

def calculate_averages(data):
    avg_temp = data['Temperature (°C)'].mean()
    avg_humidity = data['Humidity (%)'].mean()
    print(f'Average Temperature: {avg_temp:.2f}°C')
    print(f'Average Humidity: {avg_humidity:.2f}%')

# Call the function
calculate_averages(weather_data)

def days_above_temperature(data, threshold):
    days = data[data['Temperature (°C)'] > threshold]
    print(f'Days with Temperature above {threshold}°C: {len(days)}')

# Call the function
days_above_temperature(weather_data, 25)

def days_below_humidity(data, threshold):
    days = data[data['Humidity (%)'] < threshold]
    print(f'Days with Humidity below {threshold}%: {len(days)}')

# Call the function
days_below_humidity(weather_data, 55)

# Visualization
import matplotlib.pyplot as plt

# Line plot for Temperature over time
plt.figure(figsize=(10, 5))
plt.plot(weather_data['Date'], weather_data['Temperature (°C)'], color='red', label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Histogram for Humidity distribution
plt.figure(figsize=(8, 5))
plt.hist(weather_data['Humidity (%)'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.title('Humidity Distribution')
plt.show()

# Dual-axis plot for Temperature and Humidity over time
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot Temperature on the first axis (left Y-axis)
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)', color=color)
ax1.plot(weather_data['Date'], weather_data['Temperature (°C)'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis (right Y-axis) for Humidity
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Humidity (%)', color=color)
ax2.plot(weather_data['Date'], weather_data['Humidity (%)'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Add title and adjust layout
plt.title('Temperature and Humidity Over Time')
fig.tight_layout()
plt.show()
