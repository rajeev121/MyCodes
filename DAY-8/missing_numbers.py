def Missing_Numbers(nums):
    return (sum(range(len(nums)+1))-sum(nums))

numbers = [1,2,3,5,6]
result = Missing_Numbers(numbers)
print(result)