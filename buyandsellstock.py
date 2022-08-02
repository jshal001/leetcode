class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPrice = 0

        #pointers left(should point at min always) and right(max)
        left = right = 0

        while(right < len(prices)): 
            if(prices[left] > prices[right]): 
                left = right
                right += 1
            else:
                if(maxPrice < prices[right] - prices[left]):
                    maxPrice = prices[right] - prices[left] 
                right += 1

        return maxPrice




prices = [7, 6, 4, 3, 1]

solution = Solution()

print(solution.maxProfit(prices))