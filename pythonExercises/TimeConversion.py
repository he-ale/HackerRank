def timeConversion(s):
    isMorning= True if s[-2:]=="AM" else False
    if isMorning:
        if (s[0:2] == "12"):
            return "00"+s[2:-2]
        return s[0:-2]

    hour= int(s[:2])+12
    if (hour == 24):
        return "12"+s[2:-2]
    
    return str(hour)+s[2:-2]