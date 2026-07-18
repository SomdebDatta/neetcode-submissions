class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        second, third = [0, 0], [0, 0]

        for idx in range(len(prices) - 1, -1, -1):
            first = [0, 0]
            # Buy
            first[1] = max(-prices[idx] + second[0], second[1])
            # Sell
            first[0] = max(prices[idx] + third[1], second[0])

            third = second
            second = first
    
        return first[1]