def Max(num1,num2,num3):
    max = num1 if num1>num2 else num2
    max = num3 if num1>max else max

    return max

num1,num2,num3 = 20,30,10
result = Max(num1,num2,num3)
print(result)