def findSum(s):
        #code here
        p=""

        for i in s:

            if i.isdigit():

                p=p+i

            else:

                p=p+' '

        l=p.split(' ')

        sum=0

        for i in l:

            if i.isdigit():

                sum+=int(i)

        return sum

string = "1abc23"
result = findSum(string)
print(result)