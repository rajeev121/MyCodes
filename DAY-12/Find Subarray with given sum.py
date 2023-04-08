
def find_subArray(nums,length,target):
    for i in range(0, length):
        current_sum = nums[i]
        if(current_sum == target):
            print("Sum found at index", i)
            break
        else:
            # Try all subarrays starting with 'i'
            for j in range(i+1, length):
                current_sum += nums[j]
                if(current_sum == target):
                    print("Sum found between indexes", i, "and", j)
                    break
            else:
                continue
            break
    else:
        print("No subarray found with the given sum")

nums = [15,2,4,8,9,5,10,23]
length = len(nums)
target = 23

find_subArray(nums,length,target)


