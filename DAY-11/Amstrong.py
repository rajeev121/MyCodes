def check_Amstrong(number):
    num = number
    digit, sum = 0, 0
    length = len(str(num))
    for i in range(length):
        digit = int(num%10)
        num = num/10
        sum += pow(digit,length)
    if sum==number:
        return 1
    else:
        return -1
    
number = 371
result = check_Amstrong(number)
if result == 1:
    print("Its a Amstrong number")
else:
    print("It is not an amstrong number")