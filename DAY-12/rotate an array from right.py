def rotate_rightwards(nums,k):

        break_point = (len(nums) - k) % len(nums)
        nums[:] = nums[:break_point] + nums[break_point:] 
        return nums

array = [1,2,3,4,5]
k=3
result = rotate_rightwards(array,k)
print(result)