def birthday(s: list[int], d: int, m: int):
    i= 0
    result= 0
    while (i < len(s)-m+1):
        aux= 0
        j= i
        while(j < i+m):
            aux+= s[j]
            j+= 1

        if (aux == d):
            result+= 1
        
        i+=1

    return result

    