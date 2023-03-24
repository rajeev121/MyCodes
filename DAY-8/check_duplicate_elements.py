def check_Duplicate_Elements(nums):
    return (len(nums) != len(set(nums)))

nums = [1,2,3,1]
result = check_Duplicate_Elements(nums)
print(result)