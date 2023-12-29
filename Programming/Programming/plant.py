import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
file_path = "/Users/bhoumik/Desktop/Plant EP/Programming/7.csv"
data = pd.read_csv(file_path)

# Extract the data from columns 'A' and 'B'
A = data["Sample Number"]
B = data["Filtered Voltage"]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data with customizations
ax.plot(A, B, color='b', linestyle='-', marker='o', markersize=5, label='Data from data.csv')

# Set labels and title
ax.set_xlabel('X-axis Label', fontsize=12)
ax.set_ylabel('Y-axis Label', fontsize=12)
ax.set_title('Data from data.csv', fontsize=14)

# Customize the grid
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend()

# Show the plot
plt.show()
