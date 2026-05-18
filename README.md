# 📊 Gender Bias in Online Toxicity Analysis

## 🧠 Project Overview

This project investigates whether comments containing female-related expressions exhibit different toxicity levels compared to other online comments.

The main motivation of this study is to explore potential gender bias in online communication and understand how women-related language is treated on digital platforms.

The analysis includes exploratory data analysis (EDA), hypothesis testing, and machine learning methods.

---

# 🎯 Research Question

Is there a statistically significant difference in toxicity levels between comments containing female-related expressions and general online comments?

---

# 📊 Dataset

This project uses the **Jigsaw Toxic Comment Classification Dataset** from Kaggle.

Dataset link:
- https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data

The dataset contains thousands of online comments labeled with multiple toxicity categories such as:

- toxic
- severe_toxic
- obscene
- threat
- insult
- identity_hate

---

# 🔧 Data Preparation

The following preprocessing steps were applied:

- Converting text to lowercase
- Cleaning comment text
- Identifying women-related comments using keywords
- Creating a new binary feature: `women_related`
- Calculating a combined toxicity score

Women-related keywords include:

```python
["she", "woman", "women", "female", "girl"]


📈 Exploratory Data Analysis (EDA)

Several visualizations were created to better understand the dataset and compare toxicity distributions.

1. Comment Group Counts
This graph shows the number of women-related comments and other comments in the dataset.

2. Average Toxicity Score Comparison
This visualization compares the average toxicity score between women-related comments and other comments.

3. Toxicity Score Histogram
This histogram illustrates the distribution of toxicity scores across comment groups.

Most comments have relatively low toxicity scores, while a smaller number of comments contain highly toxic content.

4. Toxicity Score Boxplot
The boxplot highlights the spread, median values, and outliers in toxicity scores.

This helps visualize differences in variability between the groups.

⸻

📌 Statistical Analysis

The project includes multiple hypothesis testing methods.

Normality Test

Before applying parametric tests, normality assumptions were checked using the Shapiro-Wilk test.

The results indicated that the toxicity score distributions were not perfectly normal.

⸻

Independent T-Test

An independent t-test was used to compare average toxicity scores between:

* Women-related comments
* Other comments

The test evaluated whether the difference between the groups was statistically significant.

⸻

Mann-Whitney U Test

Since the data distribution was not perfectly normal, a non-parametric Mann-Whitney U test was also applied.

This test confirmed the statistical findings from the t-test.

⸻

🤖 Machine Learning

Machine learning methods were applied to classify toxic comments.

The notebook includes:

* TF-IDF Vectorization
* Logistic Regression
* Decision Tree Classification

The models were evaluated using:

* Accuracy score
* Classification report
* Confusion matrix

The goal was to explore whether textual patterns can help predict toxicity levels.

⸻

📌 Results

The analysis suggests that women-related comments exhibit different toxicity distributions compared to other comments.

Both the independent t-test and the Mann-Whitney U test indicated statistically significant differences between the groups.

Additionally, the machine learning models achieved reasonable performance in predicting toxic comments.

⸻

⚠️ Limitations

This project has several limitations:

* Keyword-based filtering may not fully capture context
* Some comments may contain female-related words without targeting women
* Toxicity labels may include dataset biases
* Simple machine learning models have limited contextual understanding

⸻

🚀 Future Work

Possible future improvements include:

* Using transformer-based NLP models such as BERT
* Expanding the dataset with data from multiple platforms
* Applying more advanced sentiment analysis techniques
* Improving contextual understanding of gender-related language

⸻

📓 Jupyter Notebook

The project was converted from a Python script into an executed Jupyter Notebook as requested in the milestone feedback.

Main notebook:

* DSA210_Final_Project.ipynb

⸻

▶️ How to Run

1. Install required libraries
pip install pandas numpy matplotlib scipy scikit-learn notebook

2. Download the dataset

Download the Jigsaw Toxic Comment dataset from Kaggle and place:
train.csv
inside the:
data/ folder.
3. Launch Jupyter Notebook
jupyter notebook
4. Run all notebook cells sequentially

The notebook will:

* Load the dataset
* Perform EDA
* Apply hypothesis testing
* Generate visualizations
* Train machine learning models

⸻

🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy
* Scikit-learn
* Jupyter Notebook

⸻

📂 Project Structure
DSA210-PROJECT/
│
├── data/
│   └── train.csv
│
├── result/
│
├── src/
│
├── DSA210_Final_Project.ipynb
├── analysis.py
├── README.md
│
├── comment_group_counts.png
├── average_toxicity_score_comparison.png
├── toxicity_score_histogram.png
├── toxicity_score_boxplot.png

