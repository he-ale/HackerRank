from typing import List

def plusMinus(arr: List[int]):
    resutl= [0,0,0]
    for e in arr:
        if (e > 0):
            resutl[0]+=1
        elif (e < 0):
            resutl[1]+=1
        else:
            resutl[2]+=1
    
    return [round(e/len(arr), 6) for e in resutl]