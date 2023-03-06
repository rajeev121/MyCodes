def insertAtIndex(arr,sizeOfArray,index,element):
    for i in range(sizeOfArray-1,0):
        arr[i+1] = arr[i]
    arr[index] = element
    return arr

sizeOfArray = 6
ar = [1,2,3,4,5]
index = 5
element = 90

result = insertAtIndex(ar,sizeOfArray,index,element)
print(result)