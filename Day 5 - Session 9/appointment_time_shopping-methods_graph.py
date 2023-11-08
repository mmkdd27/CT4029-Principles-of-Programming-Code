import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
reader = pd.read_excel("User_dataset.xlsx")
appointment_times = reader["Appointment_time"]
shopping_methods = reader["Shopping_method"]

plt.figure(figsize=(12, 6))

# Plotting the histogram for appointment times
plt.subplot(1, 2, 1)
plt.hist(appointment_times, bins=10, edgecolor="black")
plt.xlabel("Appointment Time")
plt.ylabel("Count")
plt.title("Histogram of Appointment Times")

plt.subplot(1, 2, 2)
plt.hist(shopping_methods, bins=10, edgecolor="black")
plt.xlabel("shopping_methods")
plt.ylabel("Count")
plt.title("Histogram of shopping_methods")

plt.tight_layout()
plt.show()
