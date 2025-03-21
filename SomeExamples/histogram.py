import matplotlib.pyplot as plt

# Sample exam scores
exam_scores = [50, 55, 60, 65, 65, 70, 70, 75, 80, 85, 85, 90, 90, 90, 95, 100]

# Create a histogram
plt.hist(exam_scores, bins=5, edgecolor="black")

# Labels
plt.xlabel("Exam Scores")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")

# Show the plot
plt.show()