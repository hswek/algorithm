import sys
from collections import deque
import heapq
#a,b,c,d,e=map(int,sys.stdin.readline().rstrip().split())
n=input()
if n=='A+':
    print(4.3)
if n=='A0':
    print(4.0)
if n=='A-':
    print(3.7)
if n=='B+':
    print(3.3)
if n=='B0':
    print(3.0)
if n=='B-':
    print(2.7)
if n=='C+':
    print(2.3)
if n=='C0':
    print(2.0)
if n=='C-':
    print(1.7)
if n=='D+':
    print(1.3)
if n=='D0':
    print(1.0)
if n=='D-':
    print(0.7)
if n=='F':
    print(0.0)