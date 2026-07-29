from typing import List

def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]):
    apples= map(lambda e: e+a, apples)
    oranges= map(lambda e: e+b, oranges)
    countApples= 0
    for apple in apples:
        if (s<=apple<=t):
            countApples+=1
    countOranges= 0
    for orange in oranges:
        if (s<=orange<=t):
            countOranges+=1
    print(countApples)
    print(countOranges)

