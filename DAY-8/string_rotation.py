def isrotated_string(s1,s2):
    for i in range(len(s1)):

            s1=s1[1:]+s1[0]

            if s1==s2:

                return 1

    return 0

str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
result = isrotated_string(str1,str2)
print(result)
