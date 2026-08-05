
def getTotalX(a: list[int], b: list[int]):
    nIni= max(a)
    nMax= min(b)
    total= 0
    while (nIni <= nMax):
        flag= True
        for e in a:
            if (nIni % e != 0):
                flag= False
                break
        if not flag:
            nIni+= 1
            continue
        else:
            for e in b:
                if (e % nIni != 0):
                    flag= False
                    break
        if not flag:
            nIni+= 1
            continue
        total+= 1
        nIni+= 1
    return total
