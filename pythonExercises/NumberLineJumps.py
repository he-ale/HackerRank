
def kangaroo(x1: int, v1: int, x2: int, v2: int):
    if(v2 == v1 and x1 != x2):
        return "NO"
        
    t= (x1-x2)//(v2-v1)
    if (t < 0):
        return "NO"
    elif((x1+v1*t) == (x2+v2*t)):
        return "YES"   
    else:
        return "NO"     

kangaroo(43, 2, 70, 2)