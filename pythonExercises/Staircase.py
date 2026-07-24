def staircase(n: str):
    rs= ""
    for i in range(1, n+1):
        rs+=" "*(n-i)+"#"*i+"\n"
    
    print(rs)
    return rs