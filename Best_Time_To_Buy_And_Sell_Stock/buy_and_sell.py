class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # we need to check if the next day is less than today
        # if it it lower on the next day we check we move the buy to that day
        # slide the window further and further
        l, r = 0, 1 # left = today, right = next day
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]: # if today is less than next day
                profit = prices[r] - prices[l] # profit will be tomorrow - today
                if maxP < profit:
                    maxP = profit
            else: # If the next day is lower price then move buy to next day
                l = r
            r += 1
        return maxP

sol = Solution()
prices=[7,1,5,3,6,4]
print(sol.maxProfit(prices))