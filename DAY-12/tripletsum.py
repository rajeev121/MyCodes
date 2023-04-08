
def find_triplet(arr,n,sum):
    for i in range(n - 2):
   
        for j in range(i + 1, n - 1):
        
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    print("Triplet is", arr[i], ",", arr[j], ",", arr[k])
                    break
    else:
        print("No triplet found")

arr = [1, 4, 45, 6, 10, 8]
n = len(arr)
target_sum = 22
find_triplet(arr,n,sum)
