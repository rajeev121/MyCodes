def rotate(nums,k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        break_point = (len(nums) - k) % len(nums)
        nums[:] = nums[break_point:] + nums[:break_point]
        return nums

array = [1,2,3,4,5]
k=3
result = rotate(array,k)
print(result)