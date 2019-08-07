def buy_sell_once(prices):
    min_so_far = prices[0]
    max_profit = 0
    for i in prices:
        max_profit = max(max_profit, i-min_so_far)
        min_so_far = min(min_so_far,i)
    return max_profit



#test_arr = [310, 300, 275, 265, 250, 230, 220,210, 205, 200]
#test_arr = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
test_arr = [0.2, 2.9, 1.3, 3.3, 1.1, 1.0, 0.3, 2.4, 2.8, 0.6, 2.4, 3.1, 1.3, 2.7, 0.6, 1.2, 1.2, 1.6, 1.0, 1.5, 2.8, 2.5, 3.1, 1.9, 1.2, 1.2, 1.1, 3.3, 2.3, 0.8, 2.8, 2.2, 0.1, 1.0, 2.2]
print(buy_sell_once(test_arr))