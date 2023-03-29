def singleNumber(nums):
        result = 0
        for num in nums:
            result += num
        
        single_number = 2 * sum(set(nums)) - result
        return single_number

array = [1,1,2,2,3,4,4]
result = singleNumber(array)
print(result)