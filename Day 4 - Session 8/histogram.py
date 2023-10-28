import pandas
import matplotlib.pyplot as plt

reader = pandas.read_excel("file_application.xlsx")
data = reader[(reader["Touches"] >= 20) & (reader["Touches"] <= 80)]
plt.figure(figsize=(8, 6))
plt.hist(data["Touches"], bins=10, edgecolor="black")
plt.xlabel("Touches")
plt.ylabel("Count")
plt.title("Histogram of Players with 20-80 Touches")
plt.show()