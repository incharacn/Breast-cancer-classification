# -*- coding: utf-8 -*-
"""Cancer Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hJ-FxQS7wnR6EQlQ_f4I7OC64XVcuZ6t
"""

#Importing the required librariws
import numpy as np
import pandas as pd
import seaborn as sns
import math as mth
import matplotlib.pyplot as plt

#Loading the dataset
df = pd.read_csv("/content/breast-cancer.csv")
df.head()

#Encoding some of the data
from sklearn.preprocessing import LabelEncoder

h = LabelEncoder()

y = h.fit_transform(df["diagnosis"])

df.info()

#Checking For Missing Values
df.isnull().sum()

#Dropping some datas in column that is not necessary
df.drop('id', axis=1, inplace=True)

(df["diagnosis"]) = y

df.head()

x = df.iloc[:, 1:].values

#Algorithm Comparision
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Define the classification models to compare
models = []
models.append(('LR', LogisticRegression()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('RF', RandomForestClassifier()))
models.append(('GB', GradientBoostingClassifier()))
models.append(('SVM', SVC()))

# Evaluate each model using 10-fold cross-validation
results = []
names = []
scoring = 'accuracy'
for name, model in models:
    cv_results = cross_val_score(model, X, y, cv=10, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Plot algorithm comparison
plt.figure(figsize=(10, 6))
sns.set(font_scale=1.2)
plt.boxplot(results, labels=names)
plt.title('Algorithm Comparison', fontsize=18)
plt.xlabel('Classification Model', fontsize=16)
plt.ylabel('Accuracy', fontsize=16)
plt.show()

"""PAIRPLOT VISUALISATION plot allow us to seeboth distribution of single variables andrelationship between two variables.

"""

sns.pairplot(df)

fig, ax = plt.subplots(figsize=(13,10))
linewidths = 2
linecolor = 'yellow'
sns.heatmap(df.corr(), linewidths=linewidths, linecolor=linecolor, annot=True, annot_kws={"size":8})
plt.title("Breast Cancer Classification")

df.keys()

#Plotting scatterplot to see the relationship between the two variables
sns.scatterplot(x = 'area_mean', y = 'smoothness_mean', hue = 'diagnosis', data=df)

"""Model Validation"""

#Logistic Regression
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a logistic regression model and fit it to the training data
logreg = LogisticRegression(random_state=42)
logreg.fit(X_train, y_train)

# Predict the labels of the testing data using the fitted model
y_pred = logreg.predict(X_test)

# Compute the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

#SVM
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create an SVM model and fit it to the training data
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train, y_train)

# Predict the labels of the testing data using the fitted model
y_pred = svm.predict(X_test)

# Compute the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

#Random Forest
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Random Forest classifier and fit it to the training data
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict the labels of the testing data using the fitted model
y_pred = rf.predict(X_test)

# Compute the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

#Gradient Booster
## Import necessary libraries
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
data = load_breast_cancer()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Create the Gradient Boosting model
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)

# Train the Gradient Boosting model on the training set
gb_model.fit(X_train, y_train)

# Predict on the testing set using the Gradient Boosting model
y_pred = gb_model.predict(X_test)

# Evaluate the performance of the Gradient Boosting model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

#KNN
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a KNN classifier and fit it to the training data
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict the labels of the testing data using the fitted model
y_pred = knn.predict(X_test)

# Compute the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target
class_names = data.target_names

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the models
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

svm = SVC()
svm.fit(X_train, y_train)

random_forest = RandomForestClassifier()
random_forest.fit(X_train, y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

gradient_boosting = GradientBoostingClassifier()
gradient_boosting.fit(X_train, y_train)

# Generate predictions for the testing data
log_reg_pred = log_reg.predict(X_test)
svm_pred = svm.predict(X_test)
random_forest_pred = random_forest.predict(X_test)
knn_pred = knn.predict(X_test)
gradient_boosting_pred = gradient_boosting.predict(X_test)

# Create confusion matrices
log_reg_cm = confusion_matrix(y_test, log_reg_pred)
svm_cm = confusion_matrix(y_test, svm_pred)
random_forest_cm = confusion_matrix(y_test, random_forest_pred)
knn_cm = confusion_matrix(y_test, knn_pred)
gradient_boosting_cm = confusion_matrix(y_test, gradient_boosting_pred)

# Plot the confusion matrices
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

sns.heatmap(log_reg_cm, annot=True, cmap="Blues", fmt="d", ax=axs[0, 0])
axs[0, 0].set_title("Logistic Regression")
axs[0, 0].set_xlabel("Predicted")
axs[0, 0].set_ylabel("Actual")
axs[0, 0].xaxis.set_ticklabels(class_names)
axs[0, 0].yaxis.set_ticklabels(class_names)

sns.heatmap(svm_cm, annot=True, cmap="Blues", fmt="d", ax=axs[0, 1])
axs[0, 1].set_title("Support Vector Machine")
axs[0, 1].set_xlabel("Predicted")
axs[0, 1].set_ylabel("Actual")
axs[0, 1].xaxis.set_ticklabels(class_names)
axs[0, 1].yaxis.set_ticklabels(class_names)

sns.heatmap(random_forest_cm, annot=True, cmap="Blues", fmt="d", ax=axs[0, 2])
axs[0, 2].set_title("Random Forest")
axs[0, 2].set_xlabel("Predicted")
axs[0, 2].set_ylabel("Actual")
axs[0, 2].xaxis.set_ticklabels(class_names)
axs[0, 2].yaxis.set_ticklabels(class_names)

sns.heatmap(knn_cm, annot=True, cmap="Blues", fmt="d", ax=axs[1, 0])
axs[1, 0].set_title("K-Nearest Neighbors")
axs[1, 0].set_xlabel("Predicted")
axs[1, 0].set_ylabel("Actual")
axs[1, 0].xaxis.set_ticklabels(class_names)
axs[1, 0].yaxis.set_ticklabels(class_names)

sns.heatmap(gradient_boosting_cm, annot=True, cmap="Blues", fmt="d", ax=axs[1, 1])
axs[1, 1].set_title("Gradient Boosting")
axs[1, 1].set_xlabel("Predicted")
axs[1, 1].set_ylabel("Actual")
axs[1, 1].xaxis.set_ticklabels(class_names)
axs[1, 1].yaxis.set_ticklabels(class_names)

plt.tight_layout()
plt.show()