def strstr(s,x):
    for i in range (len(s)):
        if(s[i:i+len(x)] == x):
            return i
    return -1

str = "geeksforgeeks"
str1 = "for"

result = strstr(str,str1)
print(result)