# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 04:37:08 2015

@author: zhyfly711
"""

'''This program is used to do binary search'''

def binarySearch(lis, target):
    '''take in an ordered list and the targeted number, return
       the index of the targeted number, or False if not exist'''
    start = 0
    end = len(lis)
    
    while start < end:
        middle = int((start + end)/2)
        if target == lis[middle]:
            return middle
        elif target < lis[middle]:
            end = middle
        else:
            start = middle + 1
    return False


print binarySearch([0], 0)
print binarySearch([0,1,4], 0)
print binarySearch([0,4,9,17], 4)
print binarySearch([0,4,8,12], 12)
print binarySearch([0,4,9,13,17], 19)