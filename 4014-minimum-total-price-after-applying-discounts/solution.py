// 159 ms | 35.2 MB
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse = True)
        x = min(len(prices),len(discounts))
        z = sum(prices[x:])
        for i in range(x):
            z+=(prices[i]*(100 - discounts[i]) / 100)
        return z
            
        