def sortByFrequency(arr):
    freq_arr = []
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if arr[j] == arr[i]:
                count += 1
        freq_arr.append((arr[i], count))
    
    for i in range(len(freq_arr)):
        for j in range(i+1, len(freq_arr)):
            if freq_arr[i][1] < freq_arr[j][1]:
                freq_arr[i], freq_arr[j] = freq_arr[j], freq_arr[i]
    
    sorted_arr = []
    for item in freq_arr:
        sorted_arr.extend([item[0]] * item[1])
    
    return sorted_arr

arr = [4, 4, 2, 5, 2, 3, 1, 1, 1]
sorted_arr = sortByFrequency(arr)
print(sorted_arr)