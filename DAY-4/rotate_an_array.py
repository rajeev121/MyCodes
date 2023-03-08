def rotate( arr, n):
    
    arr[::] = [arr[-1]] + arr[0:-1]

    return arr

array = [1,2,3,4,5]
n=5

result = rotate(array,n)
print(result)