from typing import List

def climbingLeaderboard(ranked: List[int], player: List[int]):
    scores= [ranked[0]]
    for i in range(len(ranked)):
        if scores[-1]!=ranked[i]:
            scores.append(ranked[i])
    i= len(scores)-1
    rank= len(scores)+1
    # print(scores)
    result= []
    for p in player:
        while (i > -1 and scores[i]<=p):
            rank= rank-1 if rank-1 > 0 else 1
            i-= 1
        
        result.append(rank)
    return result                 

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
