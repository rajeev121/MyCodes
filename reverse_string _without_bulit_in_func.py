def reverse_string(str):
    string = ""
    for i in range(len(str)-1,-1,-1):
        string += str[i]
    return string

string = 'Rajeev'
result = reverse_string(string)
print(result)