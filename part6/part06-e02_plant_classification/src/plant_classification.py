#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    dataset = load_iris()
    x = dataset.data
    y = dataset.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    model = naive_bayes.GaussianNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    acc = metrics.accuracy_score(y_test, y_pred)
    return acc

def main():
    print(f"Accuracy is {plant_classification()}")
    # print(plant_classification())

if __name__ == "__main__":
    main()
