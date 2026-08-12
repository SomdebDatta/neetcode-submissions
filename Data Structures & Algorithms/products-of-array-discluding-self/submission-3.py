class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0] * len(nums)
        suffix_prod = [0] * len(nums)
        ans = [0] * len(nums)

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suffix_prod[i] = prod
        
        ans[0] = suffix_prod[1]
        
        pre_prod = nums[0]

        for i in range(1, len(nums) - 1):
            
            ans[i] = pre_prod * suffix_prod[i + 1]
            pre_prod *= nums[i]

        ans[-1] = pre_prod

        return ans