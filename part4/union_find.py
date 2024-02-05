# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-29 13:00:20
# LastEditTime: 2024-02-05 12:29:47
# Description: 

class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
        self.size = [1]*n
    
    # O(logn)
    def find(self, x):
        if self.parents[x] == x:
            return x
        result = self.find(self.parents[x])
        self.parents[x] = result
        return result

    # O(logn)
    def union(self, i, j):
        p_i = self.find(i)
        p_j = self.find(j)
        if p_i == p_j:
            return
        if self.size[p_i] < self.size[p_j]:
            self.parents[p_i] = p_j
            self.size[p_j] += self.size[p_i]
        else:
            self.parents[p_j] = p_i
            self.size[p_i] += self.size[p_j]
    
    def same_component(self, i, j):
        return self.find(i) == self.find(j)

if __name__ == '__main__':

    myunionfind = UnionFind(4)
    myunionfind.union(0,3)
    myunionfind.union(1,2)
    myunionfind.union(0,2)
    print(myunionfind.parents)
    print(myunionfind.size)

    print(myunionfind.same_component(1,0))
    print(myunionfind.same_component(2,0))
    print(myunionfind.same_component(3,0))


