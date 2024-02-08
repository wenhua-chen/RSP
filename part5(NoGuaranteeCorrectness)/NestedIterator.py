# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-08 17:18:40
# LastEditTime: 2024-02-08 17:19:43
# Description: 

class NestedIterator:
    def __init__(self, nestedList):
        self.q = nestedList
    
    def next(self) -> int:
        return self.q.pop(0)
    
    def hasNext(self) -> bool:
        while self.q and type(self.q[0])!=int:
            self.q = self.q[0] + self.q[1:]
        return len(self.q) != 0

iterator = NestedIterator([[1,1],2,[1,1]])
ans = []
while iterator.hasNext():
    ans.append(iterator.next())
print(ans)



