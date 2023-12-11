from typing import List

def printDivisors(n: int) -> List[int]:
    divis=[]
    for i in range(1,n+1):
        if n%i==0:
            divis.append(i)
    return divis 
