def twoSum(numbers, target):
        sum =0
        l = len(numbers)-1
        i=0
        j=l
        while i<j:
            sum = numbers[i]+numbers[j]
            if sum == target:
                return [i,j]
            elif sum<target:
                i+=1
            elif sum>target:
                j-=1

array = [2,7,11,15]
t = 13
result=[]
result = twoSum(array,t)
print (result)