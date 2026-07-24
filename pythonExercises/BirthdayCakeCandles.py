from typing import List

def birthdayCakeCandles(candles: List[int]):
    maxValue= candles[0]
    for i in range(1, len(candles)):
        maxValue= max(maxValue, candles[i])
    
    counter= 0
    for e in candles:
        if (e == maxValue):
            counter+=1
    
    return counter