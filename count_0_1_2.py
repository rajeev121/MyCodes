def count_012(Arr):
    zero=one=two=0
    for i in range(len(Arr)):
        num = Arr[i]
        if num == 0:
            zero+=1
        elif num == 1:
            one+=1
        elif num == 2:
            two+=1
    
    i=0
    while(i<zero):
        Arr[i] = 0
        i+=1
    while(i<zero+one):
        Arr[i] = 1
        i+=1
    
    while(i<zero+one+two):
        Arr[i] = 2
        i+=1
    

    return Arr

number = [1,1,2,1,0,2,0]
result = count_012(number)
print(result)
