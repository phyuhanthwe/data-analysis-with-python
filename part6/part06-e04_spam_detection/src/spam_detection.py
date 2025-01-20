#!/usr/bin/env python3
import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def read_file(filename):
    with gzip.open(filename, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def spam_detection(random_state=0, fraction=1.0):
    ham = read_file('src/ham.txt.gz')
    spam = read_file('src/spam.txt.gz')

    ham_fraction = ham[:int(len(ham) * fraction)]
    spam_fraction = spam[:int(len(spam) * fraction)]

    data = ham_fraction + spam_fraction
    labels = [0] * len(ham_fraction) + [1] * len(spam_fraction)

    vec = CountVectorizer()
    features = vec.fit_transform(data)

    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=random_state)

    model = MultinomialNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    total = len(y_test)
    misclassified = sum(y_pred != y_test)
    
    return accuracy, total, misclassified

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
