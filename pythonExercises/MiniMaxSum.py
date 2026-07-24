from typing import List

def miniMaxSum(arr: List[int]):
    arr= sorted(arr)

    a, b= sum(arr[:-1]), sum(arr[1:])
    print(a, b)
    return (a,b)
