def searchInsert(nums, target):

        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid+1
            if target < nums[mid]:
                r = mid-1
        return l

nums = [1,3,5,6]
target = 5

result = searchInsert(nums,target)
print(result)