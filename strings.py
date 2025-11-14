def largestOddNumber(num:str):
    ans=""
    i=len(num)-1
    idx=1000000
    while(i>=0):
        if(int(num[i])%2!=0):
            idx=i
            break
        i-=1
    if(idx!=1000000):
        for j in range(idx+1):
            ans+=num[j]
    else:
        return ""
    return ans

def reverseWords(s:str):
    ans=[]
    split=s.split(' ')
    i=len(split)-1
    while(i>=0):
        if split[i]!='':
            ans.append(split[i])
        i-=1
    print(ans)


# help(str.join)
# print(dir(__builtins__))
print(reverseWords("the sky is blue  "))

# print(largestOddNumber("52"))
