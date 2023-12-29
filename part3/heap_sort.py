# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-29 12:57:51
# LastEditTime: 2023-12-29 21:44:31
# Description: sort by constructing a heap

class Heap:
    def __init__(self) -> None:
        self.arr = [None]

    def insert(self, value):
        self.arr.append(value)
        self.bubble_up(len(self.arr)-1)

    def pop(self):
        if len(self.arr) <= 1:
            return None
        if len(self.arr) == 2:
            return self.arr.pop()
        result = self.arr[1]
        self.arr[1] = self.arr.pop()
        self.bubble_down(1)
        return result

    def bubble_up(self, k):
        while (k > 1) and (self.arr[k] < self.arr[k//2]):
            self.arr[k], self.arr[k//2] = self.arr[k//2], self.arr[k]
            k = k//2

    def bubble_down(self, k):
        min_k = k
        # find min value
        for i in range(2):
            child = 2*k + i
            if (child < len(self.arr)) and (self.arr[child] < self.arr[min_k]):
                min_k = child
        # if child is smaller, swap with parent, then bubble_down again
        if min_k != k:
            self.arr[min_k], self.arr[k] = self.arr[k], self.arr[min_k]
            self.bubble_down(min_k)
    
    # make heap by bubbling down each nonleaf node
    def make_heap_fast(self, arr):
        self.arr.extend(arr)
        for i in range(len(arr)//2, 0, -1):
            self.bubble_down(i)
    
    # make heap by inserting every value
    def make_heap_slow(self, arr):
        for v in arr:
            self.arr.insert(v)


def heap_sort(arr):
    pq = Heap()
    pq.make_heap_fast(arr)
    for i in range(len(arr)):
        arr[i] = pq.pop()


arr = [12, 11, 13, 5, 6, 7]
print(arr)

heap_sort(arr)
print(arr)
