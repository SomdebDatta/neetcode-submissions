class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > 1:
                return num
