from typing import List

def diagonalDifference(arr: List[List[int]]):
    j= len(arr)-1
    result= 0
    k= 0
    for i in range(len(arr)):
        result+= arr[i][k]-arr[j][k]
        k+=1
        j-=1
    return abs(result) 