def checkPrime(num):
    for i in range(2,num):
        if num%i==0:
            return "No"
    return "Yes"

number = 11
Result=checkPrime(number)
if Result == "Yes":
    print("Prime Number")
else:
    print("Not a prime Number")
