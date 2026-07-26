
def findDigits(n):
    numbers= set(str(n))
    counter= 0
    for number in numbers:
        if (number=="0"):
            continue
        a= int(number)
        if (n % a == 0):
            counter+= str(n).count(number)
    return counter