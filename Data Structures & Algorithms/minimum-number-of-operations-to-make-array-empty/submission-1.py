class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numHash = defaultdict(int)

        for num in nums:
            numHash[num] += 1
        
        totalOps = 0

        for num in numHash:
            if numHash[num] == 1:
                return -1
            
            totalOps += math.ceil(numHash[num] / 3)
        
        return totalOps