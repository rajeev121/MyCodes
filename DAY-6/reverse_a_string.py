def reverseWords(S):
        # code here 
        result = S.split(".")[::-1] 
        return ".".join(result)

print(reverseWords("Geeks.for.Geeks.Leet"))