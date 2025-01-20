#!/usr/bin/env python3
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    df = df.apply(pd.to_numeric, errors='coerce')
    pca = PCA()
    pca.fit(df)
    v = df.var().values
    ev = pca.explained_variance_
    return v, ev

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    print("The variances are:", " ".join(f"{var:.3f}" for var in v))
    print("The explained variances after PCA are:", " ".join(f"{var:.3f}" for var in ev))
    cumulative_ev = np.cumsum(ev)
    plt.plot(range(1, len(cumulative_ev) + 1), cumulative_ev)
    plt.show()

if __name__ == "__main__":
    main()
