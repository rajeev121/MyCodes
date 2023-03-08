def plusMinus(arr):
    # Write your code here
    positive = len([i for i in arr if i > 0])
    negative = len([i for i in arr if i < 0])
    zero = len([i for i in arr if i == 0])
      
    print(str(positive/len(arr)) + '\n' + str(negative/len(arr)) + '\n'+ str(zero/len(arr)))
    
array = [1,4,0,-4,-2]
plusMinus(array)