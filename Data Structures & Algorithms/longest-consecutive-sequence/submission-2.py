class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        num_set = set(nums)
        ans = 1

        for num in nums:
            if num - 1 in num_set:
                continue
            
            start = num
            curr_total = 1
            while start + 1 in num_set:
                curr_total += 1
                start += 1
            ans = max(ans, curr_total)
        return ans