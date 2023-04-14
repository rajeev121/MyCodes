def maxProfit(prices):
        if len(prices) < 2:
            return 0
    
        min_price = prices[0]
        max_profit = 0
    
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
    
        return max_profit

stocks = [3,2,6,7,4,8,10]
result = maxProfit(stocks)
print(result)