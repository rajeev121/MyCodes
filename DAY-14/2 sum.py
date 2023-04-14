def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

array = [2,7,11,15]
t = 13
result=[]
result = twoSum(array,t)
print (result)