class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        remove_idx = []

        for i in range(2, len(nums)):
            if nums[i] == nums[i - 2]:
                remove_idx.append(i)
                
        def shift_by_one(index):
            for i in range(index, len(nums) - 1):
                nums[i] = nums[i + 1]
        ct = 0
        for idx in remove_idx:
            shift_by_one(idx - ct)
            ct += 1
        
        return len(nums) - len(remove_idx)