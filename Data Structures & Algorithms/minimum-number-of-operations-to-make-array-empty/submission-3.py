class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        operations = 0

        for num, ct in hashmap.items():
            if ct == 1:
                return -1
            
            operations += math.ceil(ct / 3)
        
        return operations