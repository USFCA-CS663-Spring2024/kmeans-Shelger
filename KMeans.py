from cluster import cluster
import numpy as np

class KMeans(cluster):
    def __init__(self, k=5, max_iterations=100):
        super().__init__()
        self.k = k
        self.max_iterations = max_iterations

    def fit(self, X):
        X = np.array(X)
        n, d = X.shape
        centroids = X[np.random.choice(n, self.k, replace = False)]
        for _ in range(self.max_iterations):
            closet = np.array([np.argmin(np.linalg.norm(x-centroids, axis=1)) for x in X])
            new_centroids = np.array([X[closet == k].mean(axis=0) if len(X[closet==k]) > 0 else centroids[k] for k in range(self.k)])
            if np.all(centroids == new_centroids):
                break
            centroids = new_centroids
        return closet.tolist(), centroids.tolist()
