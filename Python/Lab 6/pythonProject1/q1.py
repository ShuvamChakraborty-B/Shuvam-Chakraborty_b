# Step 1: Install the required libraries
# Uncomment the line below if you haven't installed the libraries yet.
# !pip install numpy pandas matplotlib scikit-learn scipy

# Step 2: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Step 3: Load the dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Step 4: Summarize the dataset
# 4.1: Dimensions of the dataset
print("Dataset Dimensions:", df.shape)

# 4.2: Peek at the data
print("\nFirst 5 rows of the dataset:")
print(df.head())

# 4.3: Statistical summary of all attributes
print("\nStatistical Summary:")
print(df.describe())

# 4.4: Breakdown of the data by the class variable
print("\nClass Distribution:")
print(df['species'].value_counts())

# Step 5: Visualize the dataset
# 5.1: Univariate plots (histograms)
df.hist(figsize=(10, 8))
plt.suptitle("Univariate Plots")
plt.show()

# 5.2: Multivariate plots (scatter plot matrix)
pd.plotting.scatter_matrix(df, figsize=(10, 10))
plt.suptitle("Multivariate Plots")
plt.show()

# Step 6: Evaluate some algorithms
# 6.1: Separate out a validation dataset
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=1
)

# 6.2: Set-up the test harness to use 10-fold cross validation
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)

# 6.3: Build multiple different models to predict species from flower measurements
models = [
    ('LR', LogisticRegression(max_iter=200)),  # max_iter is valid for LogisticRegression
    ('LDA', LinearDiscriminantAnalysis()),      # No max_iter needed for LDA
    ('KNN', KNeighborsClassifier()),
    ('CART', DecisionTreeClassifier()),
    ('NB', GaussianNB()),
    ('SVM', SVC())
]


# Initialize variables to track the best model and its accuracy
best_model = None
best_score = 0
best_model_name = ""

print("\nModel Evaluation Results:")
for name, model in models:
    scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')
    mean_score = scores.mean()
    print(f'{name}: {mean_score:.4f}')

    # Update the best model if the current model performs better
    if mean_score > best_score:
        best_score = mean_score
        best_model = model
        best_model_name = name

# Display the best model
print(f"\nBest Model: {best_model_name} with an accuracy of {best_score:.4f}")

# Step 7: Make predictions with the best model
best_model.fit(X_train, y_train)
predictions = best_model.predict(X_test)

# Step 8: Evaluate predictions
print("\nClassification Report for the Best Model:")
print(classification_report(y_test, predictions))
