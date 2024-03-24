# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-03-01 18:06:28
# LastEditTime: 2024-03-05 10:27:52
# Description: 

def normalize(data):
    means = [sum(col)/len(col) for col in zip(*data)]
    stds = [sum((x-mean)**2 for x in col)/len(col) ** 0.5 for mean, col in zip(means, zip(*data))]
    return [[(x-mean)/std for x, mean, std in zip(row, means, stds)] for row in data]

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

def normalization(data):
    means = [sum(col)/len(col) for col in zip(*data)]
    stds = [(sum((x-mean)**2 for x in col)/len(col))**0.5 for mean, col in zip(means, zip(*data))]
    return [[(x-mean)/std for mean, std, x in zip(means, stds, row)] for row in data]

if __name__ == '__main__':
    data = [[0,2],[0,0],[1,0],[5,0],[5,2]]
    data = normalize(data)
    y_pred = KMeans(k=2).fit(data)
    print(y_pred)

    