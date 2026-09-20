class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left_hash = defaultdict(int)
        right_hash = Counter(nums)

        for i in range(len(nums)):
            left_hash[nums[i]] += 1
            right_hash[nums[i]] -= 1

            left_len = i + 1
            right_len = len(nums) - left_len

            if 2 * left_hash[nums[i]] > left_len and 2 * right_hash[nums[i]] > right_len:
                return i
        
        return -1
        
