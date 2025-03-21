import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulating monthly sales data over 3 years
np.random.seed(42)
months = pd.date_range(start="2020-01", periods=36, freq="M")
sales = np.cumsum(np.random.randint(-5, 10, size=36)) + 100  # Some random variation

df = pd.DataFrame({"Date": months, "Sales": sales}).set_index("Date")

# Plot sales data
df.plot(title="Sales Over Time", ylabel="Sales")
plt.show()

# Checking trends using rolling mean
df["Rolling_Mean"] = df["Sales"].rolling(window=6).mean()
df.plot(title="Sales with 6-Month Rolling Average")
plt.show()
