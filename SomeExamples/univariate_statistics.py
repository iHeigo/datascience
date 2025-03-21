import numpy as np
import pandas as pd

# Sample exam scores
exam_scores = [50, 55, 60, 65, 65, 70, 70, 75, 80, 85, 85, 90, 90, 90, 95, 100]

# Convert to Pandas Series
scores = pd.Series(exam_scores)

# Univariate statistics
print("Mean (Average):", scores.mean())  # Average score
print("Median (Middle Value):", scores.median())  # Middle value
print("Mode (Most Common Value):", scores.mode()[0])  # Most frequent score
print("Standard Deviation (Spread):", scores.std())  # How spread out the scores are
