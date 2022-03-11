# Importing Data Analysis Library
import numpy as np
import pandas as pd
# Label encoder order is alphabetical
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
import joblib

df = pd.read_csv('income1.csv')
print(df)

print(df.isnull().sum())

for value in df:
    print(value, ":", sum(df[value] == '?'))

categorical = [var for var in df.columns if df[var].dtype == 'O']
for i in df[categorical]:
    print('\n', i, df[i].unique())

le = preprocessing.LabelEncoder()

# convert string -> float
df['workclass'] = le.fit_transform(df.workclass)
df['education'] = le.fit_transform(df.education)
df['marital_status'] = le.fit_transform(df.marital_status)
df['occupation'] = le.fit_transform(df.occupation)
df['race'] = le.fit_transform(df.race)
df['sex'] = le.fit_transform(df.sex)
df['native_country'] = le.fit_transform(df.native_country)
df['income'] = le.fit_transform(df.income)

print(df)

X = df.values[:, :-1]
y = df.values[:, 9]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100)

model = GaussianNB()
train = model.fit(X_train, y_train)

y_pred = model.predict(X_test)

filename = "Completed_model1.joblib"
joblib.dump(model, filename)

print(confusion_matrix(y_test, y_pred))
print(f'Accuracy model: {accuracy_score(y_test, y_pred) * 100:.2f}%')

print(model.predict([[22, 0, 1, 1, 7, 2, 1, 20, 7]]))
print(model.predict([[52, 2, 1, 0, 1, 2, 0, 40, 7]]))

