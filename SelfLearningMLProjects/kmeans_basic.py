from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 1], [2,1], [4, 3],
              [5, 4],[3.5,2],[4,4],[1,2.5],[5,1.5]])

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
y_kmeans = kmeans.predict(X)
print("Labels are-\n",kmeans.labels_)
#print(kmeans.cluster_centers_)

plt.scatter(X[:,0],X[:,1], c=y_kmeans,cmap='viridis')
plt.show()