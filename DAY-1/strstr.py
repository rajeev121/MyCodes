# Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s (0 based indexing)
def strstr(s,x):
    for i in range (len(s)):
        if(s[i:i+len(x)] == x):
            return i
    return -1

str = "geeksforgeeks"
str1 = "for"

result = strstr(str,str1)
print(result)
        