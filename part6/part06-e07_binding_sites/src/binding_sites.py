#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
 
from matplotlib import pyplot as plt
 
import seaborn as sns
sns.set_theme(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
import scipy
 
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label = scipy.stats.mode(real_labels[idx], keepdims=True)[0][0]
        permutation.append(new_label)
    return permutation
 
def toint(x):
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if x not in mapping:
        raise ValueError(f"Invalid character '{x}' encountered in sequence.")
    return mapping[x]

 
def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    df = df.dropna(how='all')
    # print(df.isna().sum())
    features = np.array([[toint(char) for char in seq]for seq in df['X']])
    labels = df['y'].to_numpy()
    return (features, labels)
 
def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} metric")
    plt.show()
 
def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)
    model = AgglomerativeClustering(n_clusters=2, linkage='average', metric='euclidean')
    model.fit(features)
    permutation = find_permutation(2, labels, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    acc = accuracy_score(labels, new_labels)
    # acc=accuracy_score(labels,model.labels_)   
    return round(acc, 4)
 
def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)
    hamming_matrix = pairwise_distances(features, metric='hamming')
    # plot(hamming_matrix, method='average', affinity='hamming')
    model = AgglomerativeClustering(n_clusters=2, linkage='average', metric='precomputed')
    pred_labels = model.fit_predict(hamming_matrix)
    permutation = find_permutation(2, labels, pred_labels)
    new_labels = np.array([permutation[label] for label in pred_labels])
    acc = accuracy_score(labels, new_labels)
    return round(acc, 4)
 
 
def main():
    # print(get_features_and_labels("src/data.seq"))
    print("Accuracy score with Euclidean metric is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming metric is", cluster_hamming("src/data.seq"))
    
 
if __name__ == "__main__":
    main()
 

