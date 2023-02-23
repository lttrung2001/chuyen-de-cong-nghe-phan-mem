import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
categories = ['comp.graphics', 'sci.med']
data = pd.read_json('https://raw.githubusercontent.com/selva86/datasets/master/newsgroups.json')
data = data[data.target_names.isin(categories)]
X_train, X_test, y_train, y_test = train_test_split(data['content'], data['target'], random_state=0)
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
clf = MultinomialNB().fit(X_train_counts, y_train)
X_test_counts = vectorizer.transform(X_test)
predicted = clf.predict(X_test_counts)
print("Accuracy: ", clf.score(X_test_counts, y_test))
