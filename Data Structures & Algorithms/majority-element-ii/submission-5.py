class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        ans = set()

        for n in nums:
            hashmap[n] += 1
            if hashmap[n] > len(nums) / 3:
                ans.add(n)
        
        return list(ans)