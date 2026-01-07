def formatnumber(num:str):
    res=[]
    while num:
        res.append(num[:-3])
        num = num[-3:]
    return res
print(formatnumber('1000000'))