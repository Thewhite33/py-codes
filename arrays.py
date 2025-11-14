def findMaxConsecutiveOnes(arr):
    maxcount=0
    count=0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
            maxcount=max(count,maxcount)
        else:
            count=0
    return maxcount

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))