def divisibleSumPairs(n: int, k: int, ar: list[int]):
    # Write your code here
    result= 0
    for i in range(n):
        for j in range(i+1, n):
            if ((ar[i]+ar[j]) % k == 0):
                result+= 1

    return result