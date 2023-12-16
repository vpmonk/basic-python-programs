from typing import List

def selectionSort(arr: List[int]) -> None: 
     n=len(arr)
     for i in range(n-1):
         min_index=i
         for j in range(i+1,n):
             if arr[j]<arr[min_index]:
                 min_index=j
         arr[i], arr[min_index] = arr[min_index], arr[i]  
