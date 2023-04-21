import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

# Calculate mean sales per region
sales = df[["JP_Sales", "NA_Sales", "EU_Sales"]].mean()

# Plot bar chart
sales.plot(kind="bar")
plt.title("Mean NA vs JP vs EU Sales")
plt.xlabel("Region")
plt.ylabel("Sales (millions)")
plt.show()
