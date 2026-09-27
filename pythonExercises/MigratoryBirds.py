def migratoryBirds(arr: list[int]):
    birds = {}

    for e in arr:
        if e in birds:
            birds[e] += 1
        else:
            birds[e] = 1

    result = 2**31
    maxValue = -1

    for k, v in birds.items():
        if v > maxValue or (v == maxValue and k < result):
            result = k
            maxValue = v

    return result