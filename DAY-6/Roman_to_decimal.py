def RL(S):
    N = len(S)
    for i in range(N):
        if S[i] == 'I':
            return 1
        elif S[i] == 'V':
            return 5
        elif S[i] == 'X':
            return 10
        elif S[i] == 'L':
            return 50
        elif S[i] == 'C':
            return 100
        elif S[i] == 'D':
            return 500
        elif S[i] == 'M':
            return 1000
                
    
def romanToDecimal(str): 
        # code here
    a = 0
    i = 0
    while (i < len(str)):
        x1 = RL(str[i])
        if (i + 1 < len(str)):
            x2 = RL(str[i + 1])
            if (x1 >= x2):
                a = a + x1
                i = i + 1
            else:
                a = a + x2 - x1
                i = i + 2
        else:
            a = a + x1
            i = i + 1
    return a



print(romanToDecimal("XVII"))
