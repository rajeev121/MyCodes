def kthSmallest(arr,k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        n = len(arr)


        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        for i in range(n):
            if k == i:
                return(arr[i])
            
arr = [2,3,4,1,7,5]
k=4
result = kthSmallest(arr,k)
print(result)