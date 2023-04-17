def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1

array = [1,0,2,0,4,4,0]
result = moveZeroes(array)
print(result)