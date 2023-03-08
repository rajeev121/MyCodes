def segregateElements(arr, n):
        # Your code goes here
        k=0
        j=0
        pos = []
        neg = []
        for i in range(n):
            if arr[i]>0:
                pos.append(arr[i])
            elif arr[i]<0:
                neg.append(arr[i])
            
        pos.extend(neg)
        arr[:] = pos
        
        return arr

array = [1,-2,3,-4,5,-6]
length = len(array)
result = segregateElements(array,length)
print(result)