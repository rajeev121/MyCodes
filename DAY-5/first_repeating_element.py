def find_first_repeating_element(arr):
    n = len(arr)
    last_index = [-1] * n
    min_index = n + 1
    for i in range(n):
        if last_index[arr[i]] == -1:
            last_index[arr[i]] = i
        else:
            min_index = min(min_index, last_index[arr[i]])
            last_index[arr[i]] = i
    if min_index > n:
        return -1
    else:
        return arr[min_index]

array = [3,7,5,6,1,9]
result = find_first_repeating_element(array)
print(result)