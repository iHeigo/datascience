import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data: Height (cm), Weight (kg), Age (years)
data = pd.DataFrame({
    "Height": [150, 160, 165, 170, 175, 180, 185, 190],
    "Weight": [50, 55, 60, 65, 70, 75, 80, 85],
    "Age":    [20, 35, 25, 30, 24, 50, 22, 40]
})

# Correlation matrix
print("Correlation Matrix:\n", data.corr())

# Heatmap for visualization
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
