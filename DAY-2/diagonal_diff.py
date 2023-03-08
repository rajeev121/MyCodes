def diagonalDifference(arr):
    # Write your code here
    n = len(arr)  # size of the square matrix
    left_diag = 0
    right_diag = 0
    for i in range(n):
        left_diag += arr[i][i]
        right_diag += arr[i][n-1-i]
    result = abs(left_diag - right_diag)
    return result

Array= [[1,2,3],[4,5,6],[7,8,9]]
result = diagonalDifference(Array)
print(result)
