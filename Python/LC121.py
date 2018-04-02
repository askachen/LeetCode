class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        buy = 0
        sell = 0
        profit = 0
        length = len(prices)
        for i in range(0, length-1):
            if prices[i+1] <= prices[i]:
                continue
            
            for j in range(i+1, length):
                if prices[j] - prices[i] > profit:
                    buy = i
                    sell = j
                    profit = prices[j] - prices[i]
        
        return profit
        """

        buy = 0
        profit = 0
        length = len(prices)
        for i in range(1, length):
            if prices[i] > prices[i-1]: #up
                profit = max(profit, prices[i] - prices[buy])
            else : #down
                if prices[i] < prices[buy]:
                    buy = i;            
        
        return profit

#---------------------------
a = Solution()
print a.maxProfit([7, 1, 5, 3, 6, 4])
print a.maxProfit([7, 6, 4, 3, 1])
