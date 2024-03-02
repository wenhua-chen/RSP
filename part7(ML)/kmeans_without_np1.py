# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-03-01 18:06:28
# LastEditTime: 2024-03-02 11:03:22
# Description: 

import numpy as np
import random

class KMeans(object):
    def __init__(self, k=3, max_iter=300) -> None:
        self.k = k
        self.max_iter = max_iter
    
    def fit(self, data):
        centers = self.init_centers(data)

        for _ in range(self.max_iter):
            clusters = self.create_clusters(centers, data)
            new_centers = self.create_new_centers(clusters, data)
            if self.is_converged(centers, new_centers):
                break
            centers = new_centers
        
        y_pred = self.pred_data(clusters, data)
        return y_pred
    
    def is_converged(self, centers, new_centers):
        diff = centers-new_centers
        return diff.sum() == 0
    
    def pred_data(self, clusters, data):
        y_pred = [-1] * len(data)
        for center_i, cluster in enumerate(clusters):
            for i in cluster:
                y_pred[i] = center_i
        return y_pred
    
    def init_centers(self, data):
        samples = np.random.choice(range(len(data)), self.k, replace=False)
        return data[samples]
    
    def create_clusters(self, centers, data):
        clusters = [[] for _ in range(self.k)]
        for i, point in enumerate(data):
            center_i = self.find_closest_center(point, centers)
            clusters[center_i].append(i)
        return clusters
    
    def find_closest_center(self, point, centers):
        closest_i = -1
        closest_dist = float('inf')
        for i, center in enumerate(centers):
            dist = self.cal_dist(point, center)
            if dist < closest_dist:
                closest_i = i
                closest_dist = dist
        return closest_i
    
    def cal_dist(self, p1, p2):
        return np.sqrt(np.sum((p1-p2)**2))

    def create_new_centers(self, clusters, data):
        new_centers = []
        for cluster in clusters:
            new_centers.append(np.mean(data[cluster], axis=0))
        return np.array(new_centers)

if __name__ == '__main__':
    data = np.array([[0,2],[0,0],[1,0],[5,0],[5,2]])
    y_pred = KMeans(k=2).fit(data)
    print(y_pred)

    