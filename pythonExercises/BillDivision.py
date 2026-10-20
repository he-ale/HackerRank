def bonAppetit(bill: list[int], k: int, b:int):
    total= 0

    for i in range(len(bill)):
        if (i == k):
            continue
        total+= bill[i]

    average= total//2

    result= 'Bon Appetit' if average==b else b-average

    print(result)
    return result