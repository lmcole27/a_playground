

def maxprofit(prices):
    p2 = 1 # sell pointer
    if len(prices) == 1:
        return 0
    elif len(prices) == 2:
        return max(0, prices[1]-prices[0])
    
    buy = prices[0]
    sell = prices[1]
    result = max(0, sell-buy)
    
    while p2 < len(prices):
        if prices[p2] > sell:
            sell = prices[p2]
            result = max(result, sell - buy)
        if prices[p2]< buy:
            buy = sell = prices[p2]
            result = max(result, sell - buy)
        p2 += 1
        
    return result


def maxprofit2(prices):    
    if len(prices) == 1:
        return 0
    # elif len(prices) == 2:
    #     return max(0, prices[1]-prices[0])
    
    buy = prices[0]
    p2 = 1
    result = 0

    while p2 < len(prices):
        if prices[p2] < buy:
            buy = prices[p2]
        elif prices[p2] > result:
            result = max(result, prices[p2] - buy)
        p2 += 1
    return result