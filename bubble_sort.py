def bubble_sort(array):
    #for lop to traverse to length of array
    print(len(array))
    for i in range(len(array)):
        swapped = False
    #this loop is for to compare the whole array and send the largerst number to the last of the array
        for j in range(0,len(array)-i-1):
            #if condition to check and compare the largerst number 
             if (array[j]>array[j+1]):
                tmep = array[j]
                array[j]=array[j+1]
                array[j+1]=tmep
                swapped = True
        if not swapped:
            break
data = [10, 9, 8, 7]
bubble_sort(data)
print("Sorted array is :", data)
 