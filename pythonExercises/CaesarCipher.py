UPPER= [chr(65+i) for i in range(26)] 
LOWER= [chr(97+i) for i in range(26)] 

def caesarCipher(s: str, k: int):
    res= ""
    for c in s:
        if(c.isalpha()):
            if(c.isupper()):
                key= (((ord(c)-ord('A')+k)%26)+26)%26
                res+=UPPER[key]
            else:
                key= (((ord(c)-ord('a')+k)%26)+26)%26
                res+=LOWER[key]
        else:
            res+= c
    return res

result= caesarCipher('abcdefghijklmnopqrstuvwxyz', 3)

print(result == 'defghijklmnopqrstuvwxyzabc')