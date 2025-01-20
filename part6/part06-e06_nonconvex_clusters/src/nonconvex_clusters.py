#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy


def find_permutation(n_clusters, real_labels, cluster_labels):
    permutation = []
    for i in range(n_clusters):

        idx = cluster_labels == i
        if np.sum(idx) == 0:
            permutation.append(-1)  
        else:
            new_label=scipy.stats.mode(real_labels[idx])[0]
            permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep='\t')
    X = df[['X1', 'X2']].values
    y = df['y'].values

    result = []
    for eps in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=eps)
        labels = model.fit_predict(X)

        mask = labels != -1
        num_clusture = len(set(labels[mask]))
        outliners = np.sum(labels == -1)

        if num_clusture != len(np.unique(y)):
            acc = np.nan
        else:
            permutation = find_permutation(num_clusture, y, labels)
            new_labels = np.array([permutation[label] for label in labels])
            acc = accuracy_score(y, new_labels)
        result.append({'eps': eps, 'Score': round(acc, 1), 'Clusters': num_clusture, 'Outliers': outliners})
    new_df = pd.DataFrame(result)
    new_df[['Clusters', 'Outliers']] = new_df[['Clusters', 'Outliers']].astype(float)
    # print(new_df.dtypes)
    return new_df

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
