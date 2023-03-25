def reverseWords(S):
        # code here 
        s = S.split('.')
        s = s[::-1]
        s = '.'.join(s)
        return s

string = 'My.Name.Is.Rajeev.Lochan.Rath'
result = reverseWords(string)
print(result)