import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

# Group by publisher
grouped = df.groupby("Publisher")

# Calculate mean sales per publisher
sales = grouped[["JP_Sales", "NA_Sales", "EU_Sales"]].mean()

# Sort by mean NA sales and take top 10
top_10 = sales.sort_values(by=["NA_Sales"], ascending=False).head(10)

# Plot bar chart
top_10.plot(kind="bar")
plt.title("Average JP/NA/EU sales per publisher (Top 10)")
plt.xlabel("Publisher")
plt.ylabel("Sales (millions)")
plt.show()
