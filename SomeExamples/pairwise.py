import pandas as pd

# Sample data: Study Hours vs. Exam Score (correlated)
# Ice Cream Sales vs. Exam Score (not correlated)
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Increasing pattern
    "Exam_Score":  [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],  # Also increasing → correlated
    "Ice_Cream_Sales": [100, 150, 80, 200, 50, 300, 90, 110, 400, 250]  # Random numbers → not correlated
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df.corr()

print("Pairwise Correlation:\n", correlation)