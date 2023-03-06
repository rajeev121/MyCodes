# Split the binary string into substrings with equal number of 0s and 1s


def maxSubStr(str):
        #Write your code here
    count_zero=0
    count_one=0
    count=0
    for i in str:
        if i=='0':
            count_zero+=1
        elif i=='1':
            count_one+=1
        if count_zero==count_one :
            count+=1
            count_zero=0
            count_one=0
            
    return count if count_zero==count_one else -1

string = "101110001010"
result = maxSubStr(string)
print(result)