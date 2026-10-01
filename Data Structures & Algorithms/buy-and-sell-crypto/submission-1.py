class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=1000000
        maxprice=0
        for price in prices:
            minprice=min(minprice,price)
            profit=price-minprice
            maxprice=max(maxprice,profit)
        return maxprice







            

        