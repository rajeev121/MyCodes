def recursum(sum,num1,num2):
  if num1 > num2:
    return sum
  return num1 + recursum(sum,num1+1,num2)

num1=2
num2=5
sum=0
result = recursum(sum,num1,num2)
print(result)