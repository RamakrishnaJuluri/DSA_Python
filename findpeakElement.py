def findpeakElement(array,n):
    if(n == 1):
        return 0
    if(array[0] >= array[1]):
        return 0
    if(array[n-1] >= array[n-2]):
        return n-1
    for i in range(1, n-1):
        if(array[i]>=array[i-1] and array[i]>=array[i+1]):
            return array[i]
array = [ 10, 20, 15, 2, 23, 90, 67]
n = len(array)
print("the peak element is ", findpeakElement(array,n))
    
