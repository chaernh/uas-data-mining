import pandas as pd
from sklearn.cluster import KMeans

# Data awal
data = {
    'Sepal Length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9],
    'Sepal Width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1]
}

df = pd.DataFrame(data)

# Inisialisasi KMeans dengan K=2
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit model ke data
kmeans.fit(df)

# Dapatkan label cluster dan centroid
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Tampilkan hasil
print("Label Cluster:")
print(labels)
print("\nCentroid:")
print(centroids)