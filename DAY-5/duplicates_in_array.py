def duplicates(arr, n): 
    dd = {}
    for val in arr:
        if val in dd:
            dd[val] += 1
        else:
            dd[val] = 1

    repeated_elements = [key for key, value in dd.items() if value > 1]

    return sorted(repeated_elements) if repeated_elements else [-1]

N = 5
a= [2,3,1,2,3]
result = duplicates(a,N)
print(result)
