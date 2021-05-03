#!/bin/python3

import sys

def uglyOrBeautiful(a):
    Len = len(a)
    SetLen = len(set(a))
    if Len!=SetLen:
        return "Ugly"
    Acpy = a.copy()
    Acpy.sort()
    if a==Acpy:
        return "Ugly"
    for i in a:
        if (i<1 or i>n):
            return "Ugly"
    return "Beautiful"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        result = uglyOrBeautiful(a)
        print(result)
