def findFrequency (arr, n, x):
    # Your Code Here
    count = 0
    for i in range(n):
        if arr[i] == x:
            count+=1
    return count

array = [1,-2,3,-4,5,-6,5,3,5,1,3,5]
length = len(array)
element = 5
result = findFrequency(array,length,element)
print(result)