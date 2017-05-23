#!/bin/python
#https://www.hackerrank.com/contests/101hack49/challenges/cartesian-country
#by oz

import sys

def getMaxBridges(x1, y1, x2, y2, xC, yC):
    # Complete this function
    
    if (xC==x1 and yC==y1) or (xC==x2 and yC==y1) or (xC==x1 and yC==y2) or (xC==x2 and yC==y2):
        return 0
    
    elif xC==x1 or xC==x2:
        uno=abs(yC-y1)
        dos=abs(yC-y2)
        if uno>dos:
            return dos
        else:
            return uno
    elif yC==y1 or yC==y2:
        uno=abs(xC-x1)
        dos=abs(xC-x2)
        if uno>dos:
            return dos
        else:
            return uno
    
    else:
        uno=abs(xC-x1)
        dos=abs(xC-x2)
        
        tres=abs(yC-y1)
        cuatro=abs(yC-y2)
        
        valx=0
        valy=0
        
        if uno>dos:
            valx=dos
        else:
            valx=uno
        
        if tres>cuatro:
            valy=cuatro
        else:
            valy=tres
        
        if valx<valy:
            fixX=valx*2+1
            return fixX*valy+valx
        else:
            fixY=valy*2+1
            return fixY*valx+valy
            
            

#  Return the maximum number of bridges the Rulers will commission.
x1, y1 = raw_input().strip().split(' ')
x1, y1 = [long(x1), long(y1)]
x2, y2 = raw_input().strip().split(' ')
x2, y2 = [long(x2), long(y2)]
xC, yC = raw_input().strip().split(' ')
xC, yC = [long(xC), long(yC)]
result = getMaxBridges(x1, y1, x2, y2, xC, yC)
print(result)
