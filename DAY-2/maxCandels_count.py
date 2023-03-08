def birthdayCakeCandles(candles):
    # Write your code here
    max_candles = max(candles)
    return(candles.count(max_candles))

arr = [4,7,3,7,3,5]
result = birthdayCakeCandles(arr)
print(result)
