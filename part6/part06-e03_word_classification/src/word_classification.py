#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
    char_to_index = {char: index for index, char in enumerate(alphabet)}
    # print(char_to_index)
    feature_matrix = np.zeros((len(a), len(alphabet)), dtype=int)
    for i, word in enumerate(a):
        for char in word:
            if char in char_to_index:
                feature_matrix[i, char_to_index[char]] += 1
    return feature_matrix

def contains_valid_chars(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyzäö-")
    return all(char in alphabet for char in s)

def get_features_and_labels():
    finnish_words = load_finnish()
    eng_words = load_english()
    alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
    finnish_words = [word.lower() for word in finnish_words if contains_valid_chars(word.lower())]
    eng_words = [word.lower() for word in eng_words if word[0].islower() and contains_valid_chars(word.lower())]
    all_words = finnish_words + eng_words
    labels = [0] * len(finnish_words) + [1] * len(eng_words)
    x = get_features(np.array(all_words))
    y = np.array(labels)
    return x, y


def word_classification():
    x, y = get_features_and_labels()
    model = MultinomialNB()
    cv = model_selection.KFold(5, shuffle=True, random_state=0)
    score = cross_val_score(model, x, y, cv=cv)
    return score


def main():
    print("Accuracy scores are:", word_classification())
    # print(get_features('abc'))
    # print(contains_valid_chars('ad  '))
    # print(get_features_and_labels())

if __name__ == "__main__":
    main()
