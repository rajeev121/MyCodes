def subArraySum(a, n, s): 
       #Write your code here
       prev=0
       total=a[0]
       i=1
       
       while True:
            # print(total)
            if total==s:
               return [prev+1,i]
            if total>s and prev<i-1:
                total=total-a[prev]
                prev+=1
                continue
            
            if i>n-1:
                return [-1]
            total+=a[i]
            i+=1

array = [1,2,3,4,5]
n=5
s=5
result = subArraySum(array,n,s)
print(result)