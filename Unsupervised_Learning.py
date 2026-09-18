import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler

# 1. Load / Generate raw unlabeled dataset (Features X only)
# Creating a dummy dataset with 10 samples and 2 features for demonstration
X, _ = make_blobs(n_samples=10, centers=3, n_features=2, random_state=42)

# 2. Preprocess data (Scale features to [1] range) [2, 3]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 3. Initialize unsupervised clustering model (k-Means with K=3 clusters) [4]
model = KMeans(n_clusters=3, random_state=42)

# 4. Fit the model to find underlying cluster centroids [4]
model.fit(X_scaled)

# 5. Predict / assign cluster labels for every data point [4, 5]
cluster_labels = model.predict(X_scaled)

# 6. Display cluster assignments
for sample_id, cluster_id in enumerate(cluster_labels):
  print(
      f"Sample {sample_id}: {X_scaled[sample_id].round(2)} --> Assigned to Cluster {cluster_id}"
  )