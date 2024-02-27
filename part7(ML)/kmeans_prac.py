# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-27 19:57:07
# LastEditTime: 2024-02-27 20:52:26
# Description: 

class KMeans(object):
    def __init__(self, k=3, max_iter=300):
        self.k = k
        self.max_iter = max_iter
    
    def fit(self, data):
        centers = self.create_centers(data)

        for _ in range(self.max_iter):
            clusters = self.create_clusters(centers, data)
            new_centers = self.create_new_centers(clusters, data)
            if self.is_converged(centers, new_centers):
                break
            centers = new_centers
        y_pred = self.get_pred_labels(clusters, data)
        return y_pred
    
    def get_pred_labels(self, clusters, data):
        y_pred = [-1] * len(data)
        for center_i, cluster in enumerate(clusters):
            for index in cluster:
                y_pred[index] = center_i
        return y_pred

    def create_centers(self, data):
        centers = [data[i] for i in range(self.k)]
        return centers
    
    def create_new_centers(self, clusters, data):
        new_centers = []
        for cluster in clusters:
            cluster = [data[i] for i in cluster]
            new_center = [float(sum(col))/len(col) for col in zip(*cluster)]
            new_centers.append(new_center)
        return new_centers
    
    def is_converged(self, centers, new_centers):
        diff = 0
        for i in range(self.k):
            center = centers[i]
            new_center = new_centers[i]
            for v1,v2 in zip(center, new_center):
                diff += (v1-v2)
        return diff == 0
    
    def create_clusters(self, centers, data):
        clusters = [[] for _ in range(self.k)]
        for i, point in enumerate(data):
            center_i = self.find_closest_center(point, centers)
            clusters[center_i].append(i)
        return clusters

    def find_closest_center(self, point, centers):
        center_i = -1
        min_dist = float('inf')
        for i, center in enumerate(centers):
            dist = self.get_distance(point, center)
            if dist < min_dist:
                center_i = i
                min_dist = dist
        return center_i
    
    def get_distance(self, point, center):
        total = 0
        for v1, v2 in zip(point, center):
            total += (v1-v2)**2
        return total ** 0.5

if __name__ == '__main__':
    data = [[0,2],[0,0],[1,0],[5,0],[5,2]]
    y_pred = KMeans(2).fit(data)
    print(y_pred)

    
