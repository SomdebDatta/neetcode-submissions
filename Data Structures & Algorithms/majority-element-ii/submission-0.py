class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        ans = []

        for num in nums:
            hashmap[num] += 1
        
        for num, ct in hashmap.items():
            if ct > len(nums) / 3:
                ans.append(num)
        
        return ans