# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-21 12:31:39
# LastEditTime: 2023-12-21 12:36:12
# Description: 

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self) -> None:
        if Singleton.__instance != None:
            raise Exception('This class is a singleton!')
        else:
            Singleton.__instance = self

s = Singleton()
print(s)

print(Singleton.getInstance())
print(Singleton.getInstance())


