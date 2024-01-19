# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-19 11:25:18
# LastEditTime: 2024-01-19 11:30:22
# Description: 

def gcd1(a,b):
    while b > 0:
        a, b = b, a%b
    return a

def gcd2(a,b):
    if b == 0:
        return a
    return gcd2(b, a%b)

print(gcd2(6,9))
print(gcd2(9,6))
print(gcd2(6,10))
print(gcd2(6,11))