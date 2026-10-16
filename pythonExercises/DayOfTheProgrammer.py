from datetime import datetime, timedelta

def dayOfProgrammer(year):
    if  (year <= 1917):
        days= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if(year%4 == 0):
            days[1]= 29

        n= 256
        for i in range(len(days)):
            if (n<days[i]):
                return f"{n:02d}.{i+1:02d}.{year}"
            else:
                n-= days[i]

    else:
        result= datetime(year, 1 , 1)+ timedelta(days=255)
    return result.strftime("%d.%m.%Y")

print(dayOfProgrammer(1918))
