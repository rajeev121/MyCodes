def checkPangram(string):
    char_set = set()
     
    for ch in string:
        if ch >= 'a' and ch <= 'z':
            char_set.add(ch)
     
        if ch >= 'A' and ch <= 'Z':
            ch = ch.lower()
            char_set.add(ch)
    if len(char_set) == 26:
        return 26
    return -1
 
string = "The quick brown fox jumps over the lazy dog"
if checkPangram(string) == 26:
    print("It is a Pangram")
else:
    print("It is Not a Pangram")