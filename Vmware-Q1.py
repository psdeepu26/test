#!/bin/python3

import math
import os
import random
import re
import sys

#

# Complete the 'commonSubstring' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#

def commonSubstring(a, b):
    c1 = len(a)
    c2 = len(b)
    for i in range(min(c1,c2)):
        checkCommonString(a[i], b[i])

def checkCommonString(s1,s2):
    common = len(set(s1).intersection(s2))
    if common == 0:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    commonSubstring(a, b)
