class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        st = prices[:]
        
        for i in range(n):
            j = i + 1
            while j < n and prices[j] > prices[i]:
                j += 1
            if j < n:
                st[i] = prices[i] - prices[j]
        return st
           