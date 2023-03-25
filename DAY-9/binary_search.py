def binarysearch(arr, n, k):
    start = 0
    end = n-1
    mid = int(start + (end-start)/2)
    while start <= end:
        if arr[mid] == k:
            return mid
        if k > arr[mid]:
            start = mid+1
        else:
            end = mid-1
        mid = int(start + (end-start)/2)
    return -1

num = [1, 2, 3, 4, 5, 6]
k = 4
length = len(num)
result = binarysearch(num, k, length)
print(result)
