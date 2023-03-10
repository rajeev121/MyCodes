def isRotated(str1,str2):
        #code here
        first_string =str2[2:] + str2[:2]
        second_string =str1[2:] + str1[:2]
        if str1 == first_string or str2 == second_string:
            return 1
        else:
            return 0
        
print(isRotated("GeeksforGeeks","geeksgeeksfor"))
print(isRotated("amazon","azonam"))