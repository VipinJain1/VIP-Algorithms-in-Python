#Complete the timeConversion function in the editor below. It should return a new string 
#representing the input time in 24 hour format.
#timeConversion has the following parameter(s):
#s: a string representing time in  hour format

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    cnt =1
    for i in range (n):
        for i in range(n-cnt):
            print (' ', end = "")
        for i in range (cnt):
            print ('#', end = "")
        print (end = "\n")    
        cnt = cnt + 1



if __name__ == '__main__':
    n = int(input())
    staircase(n)

