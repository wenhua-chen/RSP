# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-27 13:08:13
# LastEditTime: 2024-03-01 18:05:39
# Description: 


# randomly select centroid start points, uniformly distributed across domain of the dataset
# iterate, adusting centroids until converged or until passed max_iter


import numpy as np
class KMeans(object):
    def __init__(self, k=3, max_iter=300):
        self.k = k
        self.max_iter = max_iter

    def centroids_init(self, data):
        return np.array([data[i] for i in range(self.k)])

    def create_clusters(self, centroids, data):
        clusters = [[] for _ in range(self.k)]
        for i, point in enumerate(data):
            clf_i = self.closest_centroid(point, centroids)
            clusters[clf_i].append(i)
        return clusters
    
    def closest_centroid(self, point, centroids):
        closest_i = 0
        closest_dist = float('inf')
        for i, centroid in enumerate(centroids):
            dist = self.get_dist(point, centroid)
            if dist < closest_dist:
                closest_i = i
                closest_dist = dist
        return closest_i

    def get_dist(self, p1, p2):
        return np.sqrt(np.sum((p1-p2)**2))

    def create_new_centroids(self, clusters, data):
        new_centroids = []
        for cluster_i in clusters:
            new_centroid = np.mean(data[cluster_i], axis=0)
            new_centroids.append(new_centroid)
        return np.array(new_centroids)

    def is_converged(self, centroids, new_centroids):
        diff = centroids - new_centroids
        return diff.sum() == 0
    
    def get_cluster_labels(self, clusters, data):
        y_pred = [-1] * len(data)
        for clf, cluster in enumerate(clusters):
            for i in cluster:
                y_pred[i] = clf
        return y_pred
    
    def fit(self, data):
        centroids = self.centroids_init(data)

        for _ in range(self.max_iter):
            clusters = self.create_clusters(centroids, data)
            new_centroids = self.create_new_centroids(clusters, data)
            if self.is_converged(centroids, new_centroids):
                break
        
        return self.get_cluster_labels(clusters, data)

if __name__ == '__main__':
    data = np.array([[0,2],[0,0],[1,0],[5,0],[5,2]])
    labels = KMeans(2, 10).fit(data)
    print(labels)


