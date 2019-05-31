
#Function Description
#Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
#miniMaxSum has the following parameter(s):
#arr: an array of  integers
#Input Format
#A single line of five space-separated integers.
#Constraints
#Output Format
#Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minSum = sum((sorted (arr))[:4])
    maxSum = sum((sorted (arr))[1:])
    print (minSum,maxSum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
