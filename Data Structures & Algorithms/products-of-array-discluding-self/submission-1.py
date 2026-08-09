class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = [0] * len(nums)
        ans = [0] * len(nums)
        prod = 1

        for num in nums:
            prefix_prod.append(prod)
            prod *= num
        prod = 1
        for idx in range(len(nums) - 1, -1, -1):
            suffix_prod[idx] = prod
            prod *= nums[idx]
        
        for i in range(len(nums)):
            if i == 0:
                ans[i] = suffix_prod[i]
                continue
            if i == len(nums) - 1:
                ans[i] = prefix_prod[i]
                continue
            ans[i] = prefix_prod[i] * suffix_prod[i]
        
        return ans