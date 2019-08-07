def buy_sell_twice(prices, N):
    sell_index = -1*len(prices)
    while N > 0:
        max_profit = 0;  min_so_far = float('inf')
        n_prices = prices[sell_index:]
        for j,i in enumerate(n_prices):
            if (i-min_so_far) > max_profit:
                sell_index = j
            max_profit = max(max_profit, i-min_so_far)
            min_so_far = min(min_so_far, i)

        print (max_profit)
        N -= 1
A = [12,11,13,9,12,8,14,13,15]
print(buy_sell_twice(A, 2))