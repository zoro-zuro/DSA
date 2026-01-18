class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices
        st = []
        for i , price in enumerate(prices):
            while st and ans[st[-1]] >= price:
                j = st.pop()
                ans[j] -= price
            st.append(i)
        return ans
           