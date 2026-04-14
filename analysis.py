# DSA 210 Project
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# 1. Read dataset
df = pd.read_csv("/Users/busranurenci/Downloads/archive/train.csv")

# 2. Show basic info
print("First 5 rows:")
print(df.head())
print("\nColumns:")
print(df.columns)

# 3. Create women_related feature
keywords = ["she", "woman", "women", "female", "girl"]

def is_women_related(text):
    text = str(text).lower()
    for k in keywords:
        if k in text:
            return 1
    return 0

df["women_related"] = df["comment_text"].apply(is_women_related)

# 4. Create a combined toxicity score
toxicity_columns = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
df["toxicity_score"] = df[toxicity_columns].mean(axis=1)

# 5. Compare group averages
women_avg = df[df["women_related"] == 1]["toxicity_score"].mean()
other_avg = df[df["women_related"] == 0]["toxicity_score"].mean()

print("\nAverage toxicity score:")
print("Women-related:", women_avg)
print("Others:", other_avg)

# 6. Prepare groups for hypothesis test
women_group = df[df["women_related"] == 1]["toxicity_score"]
other_group = df[df["women_related"] == 0]["toxicity_score"]

# 7. T-test
t_stat, p_value = ttest_ind(women_group, other_group, equal_var=False)

print("\nT-test results:")
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("The difference is statistically significant.")
else:
    print("The difference is not statistically significant.")

# 8. Graph 1: Average toxicity comparison
labels = ["Women-related", "Others"]
values = [women_avg, other_avg]

plt.figure(figsize=(8, 5))
plt.bar(labels, values)
plt.title("Average Toxicity Score Comparison")
plt.ylabel("Average Toxicity Score")
plt.xlabel("Comment Group")
plt.savefig("average_toxicity_score_comparison.png")
plt.show()

# 9. Graph 2: Number of comments in each group
women_count = df["women_related"].sum()
other_count = len(df) - women_count

counts = [women_count, other_count]

plt.figure(figsize=(8, 5))
plt.bar(labels, counts)
plt.title("Number of Comments by Group")
plt.ylabel("Count")
plt.xlabel("Comment Group")
plt.savefig("comment_group_counts.png")
plt.show()

# 10. Graph 3: Histogram
plt.figure(figsize=(8, 5))
plt.hist(women_group, bins=20, alpha=0.7, label="Women-related")
plt.hist(other_group, bins=20, alpha=0.7, label="Others")
plt.title("Distribution of Toxicity Scores")
plt.xlabel("Toxicity Score")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("toxicity_score_histogram.png")
plt.show()

# 11. Graph 4: Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot([women_group, other_group], tick_labels=["Women-related", "Others"])
plt.title("Toxicity Score Distribution by Group")
plt.ylabel("Toxicity Score")
plt.savefig("toxicity_score_boxplot.png")
plt.show()
