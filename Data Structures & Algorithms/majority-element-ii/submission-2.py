class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_hash = defaultdict(int)

        for num in nums:
            num_hash[num] += 1
        
        ans = []
        for num, ct in num_hash.items():
            if ct > len(nums) / 3:
                ans.append(num)
        
        return ans