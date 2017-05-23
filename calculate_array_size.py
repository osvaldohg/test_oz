#!/bin/python
#https://www.hackerrank.com/contests/101hack49/challenges/calculate-array-size
#by oz

import sys

def getArrayKb(n, d):
    # Complete this function
    sum=1
    for i in d:
        sum=sum*i
    
    sum=sum*4
    return sum/1024

#  Return the size of the multidimensional array in kilobytes. Return only the integer part.
n = int(raw_input().strip())
d = map(int, raw_input().strip().split(' '))
result = getArrayKb(n, d)
print(result)
