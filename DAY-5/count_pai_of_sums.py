def getPairsCount(arr, n, k):
        c=0
        mp={}
        for i in range(n):
            target=k-arr[i]
            if target in mp:
                c+=mp[target]
            if arr[i] in mp:
                mp[arr[i]]+=1
            else:
                mp[arr[i]]=1
        return c

array = [1,2,3,2,1]
N = len(array)
K = 4
result = getPairsCount(array,N,K)
print(result)