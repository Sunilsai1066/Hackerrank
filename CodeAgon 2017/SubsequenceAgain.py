#!/bin/python3

import sys

def subsequenceAgain(s, k):
    Lis = []
    for i in s:
        if i not in Lis:
            Val = s.count(i)
            if Val>=k:
                Lis.append(i)
    SetChar = set(s)
    FinLis = list(SetChar-set(Lis))
    for j in FinLis:
        s = s.replace(j,"")
    return s
    
    

if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    result = subsequenceAgain(s, k)
    print(result)
