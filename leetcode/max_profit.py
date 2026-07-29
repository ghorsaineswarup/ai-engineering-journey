def maxProfit(prices):
     
    lowest_price = prices[0]

   
    best_profit = 0

    
    for price in prices[1:]:
 
        if price < lowest_price:
            lowest_price = price

      
        else:
            profit = price - lowest_price
 
            if profit > best_profit:
                best_profit = profit

    return best_profit

 
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))   