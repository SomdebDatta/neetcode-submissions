class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = 0
        low, high = 1, max(piles)

        def can_eat(bananas):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / bananas)
                if hours > h:
                    return False
            return True

        while low <= high:
            mid = (low + high) // 2
            if can_eat(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans