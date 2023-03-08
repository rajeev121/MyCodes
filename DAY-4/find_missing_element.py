def MissingNumber(array,n):
        # code here
        array.sort()
        for i in range(n-1):
            if i+1 != array[i]:
                return i+1

array = [1,2,4,5]
n=5

result = MissingNumber(array,n)
print(result)