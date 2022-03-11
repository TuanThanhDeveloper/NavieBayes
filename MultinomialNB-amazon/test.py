import pickle
import re

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

cv = CountVectorizer(max_features=2500)
# reading data
df = pd.read_csv("AmazonMobile.csv", encoding="ISO-8859-1")
#df = pd.read_csv("Corona_NLP_train.csv", encoding="ISO-8859-1")
df.tail()

# take a look at the type, number of columns, entries, null values etc..
df.info()
df.isna().sum()

# value percentage
print("Value Percentage: \n", df['Sentiment'].value_counts() * 100 / len(df['Sentiment']))

# Chuyển các từ có nghĩa giống nhau thành 1 dạng: ví dụ include, included -> include
ps = PorterStemmer()

stop_words = stopwords.words("english")


def remove_stopwords(text):
    """Lọc lại các tweet

    returns: corpus of stemmed words"""

    text = re.sub('^a-zA-Z', ' ', text)
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stop_words]
    text = ' '.join(text).replace('  ', ' ')
    return text


# Lọc tweet

df["removed_stopwords"] = df.OriginalTweet.apply(remove_stopwords)
print('\n', df["removed_stopwords"])

# chuyển đổi text thành ma trận
# A = cv.fit_transform([df.removed_stopwords[2]]).toarray()

X = cv.fit(df.removed_stopwords)

A = X.transform(df.removed_stopwords)
tfidfTransformer = TfidfTransformer().fit(A)
title_tfid = tfidfTransformer.transform(A)

X_train, X_test, y_train, y_test = train_test_split(title_tfid, df.Sentiment, test_size=0.3, shuffle=False)
model = MultinomialNB().fit(X_train, y_train)
multi_pred = model.predict(X_test)

score_multi = accuracy_score(multi_pred, y_test)
print(f"\nMultinomialNB Accuracy Score: {score_multi * 100:.2f}%")

FileName = "model1.clf"
pickle.dump(model, open(FileName, "wb"))

#FileName = "model11.clf"
#pickle.dump(model, open(FileName, "wb"))