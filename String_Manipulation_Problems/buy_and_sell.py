class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #iterate through array, store lowest and calculate profit
        # can check profit, to profit we need lower to be lower than current price
        # Find min and max of the array, so iterate through and compare min vs max, then calculate profit and return
        #hashmap where key is day value is price
        # check if key > currents key and if price is lower / higher that day update
        myHash = {}
        day = 0
        profit = 0
        minPrice = [prices[0], 0]
        maxPrice = [prices[1], 1]
        
        for i, price in enumerate(prices):
            myHash[i] = price
        for key, value in myHash.items():
            #key is day, value is price
            if value > maxPrice[0] and key > minPrice[1]: # day to the sell
                maxPrice[0] = value
                maxPrice[1] = key
            elif value < minPrice[0] and key < maxPrice[1]: # day to buy
                minPrice[0] = value
                minPrice[1] = key
        if maxPrice[0] - minPrice[0] < 0:
            return 0
        profit = maxPrice[0] - minPrice[0]

        return profit

sol = Solution()
prices=[7,1,5,3,6,4]
print(sol.maxProfit(prices))