

def findIndex(str):
        # Your code goes here
        N = len(str)
        count=0
        for i in range(N):
            if str[i]==')':
                count+=1
        return count

print(findIndex("(())))("))