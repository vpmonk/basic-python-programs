from math import *
from collections import *
from sys import *
from os import *

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("true")
else:
    print("false")            
