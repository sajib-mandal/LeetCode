def maxProfit(prices):
    if not prices:
        return 0
    currPro = 0
    prev = prices[0]

    for price in prices:
        if prev > price:
            prev = price
        currPro = max(currPro, price - prev)
    return currPro
    
  

print(maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(maxProfit([7, 6, 4, 3, 1])) # 0
