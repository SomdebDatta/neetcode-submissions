class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def checkParity(a, b):
            if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
                return False
            return True
        

        for i in range(len(nums) - 1):
            if not checkParity(nums[i], nums[i + 1]):
                return False
        return True