class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        for i , price in enumerate(prices):
            while st and prices[st[-1]] >= price:
                j = st.pop()
                prices[j] -= price

            st.append(i)
        return prices
           