def sortColors(nums):
        zero=one=two=0
        for i in range (len(nums)):
            num = nums[i]
            if num == 0:
                zero+= 1
            elif num == 1:
                one+= 1
            elif num == 2:
                two+= 1
            
        i=0
        while(i<zero):
            nums[i] = 0
            i+=1
        while(i<zero+one):
            nums[i] = 1
            i+=1
        while(i<zero+one+two):
            nums[i] = 2
            i+=1
        
        return nums

nums = [1,0,2,1,0,1,2]
result = sortColors(nums)
print(result)