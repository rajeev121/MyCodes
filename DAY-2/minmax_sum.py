def miniMaxSum(arr):
    # Write your code here
    return([sum(arr)-max(arr),sum(arr)-min(arr)])

array=[1,2,3,4,5]
result = miniMaxSum(array)
print(result)