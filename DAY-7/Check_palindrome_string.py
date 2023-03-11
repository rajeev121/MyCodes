def Palindrome(str):
    
    if str[:] == str[::-1]:
        print("String is Palindrome")
    else:
        print("String is not palindrome")

string = "HAMAH"
Palindrome(string)
