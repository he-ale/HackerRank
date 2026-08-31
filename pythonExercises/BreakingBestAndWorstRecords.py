from typing import List

def breakingRecords(scores: List[int]):
    if (len(scores) == 1):
        print("0 0")
        return 0, 0

    worst= scores[0]
    best= scores[0]
    countWorst= 0
    countBest= 0
    for i in range(1, len(scores)):
        if (worst > scores[i]):
            countWorst+= 1
            worst= scores[i]
        elif (best < scores[i]):
            countBest+= 1
            best= scores[i]

    print(f"{countBest} {countWorst}")
    return countBest, countWorst