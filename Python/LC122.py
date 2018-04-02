class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = -1
        profit = 0
        length = len(prices)
        
        for i in range(length-1):
            # go down
            if prices[i+1] <= prices[i]:
                if buy != -1:
                    profit += prices[i] - prices[buy] #sell
                    buy = -1 #empty hand
                continue
            
            # go up
            if buy == -1:
                buy = i
                print 'buy:', buy

        # sell last stock
        if buy != -1:
            profit += prices[length-1] - prices[buy] #sell
        
        return profit

#---------------------------
a = Solution()
print a.maxProfit([7, 1, 5, 3, 6, 4])
print a.maxProfit([1,2])
