def findPairs(list,n,sum):
    for i in range(0,n):
        for j in range(1,n-1):
            value = list[i]+list[j]
            if(value == sum):
                print(list[i],list[j])

list = [1,2,3,5,6,7,4,6,7]
n = len(list)
findPairs(list,n,5)
