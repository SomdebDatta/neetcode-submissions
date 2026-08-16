class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_hash = defaultdict(int)
        ans = set()

        for num in nums:
            num_hash[num] += 1
            if num_hash[num] > len(nums) / 3:
                ans.add(num)
        
        return list(ans)