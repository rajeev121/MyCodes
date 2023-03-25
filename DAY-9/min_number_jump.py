def minJumps(self, arr, n):
    for i in range(0, len(arr)):
        value = sum(arr[0:i])
        if value == n:
            return i
        elif value > n:
            return i-1
    return -1

N = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
result = minJumps(arr, N)
print(result)
