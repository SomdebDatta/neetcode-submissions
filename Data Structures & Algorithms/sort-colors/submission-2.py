class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        print(hashmap)
        idx = 0
        color = 0

        while idx < len(nums) and color < 3:
            if hashmap[color] == 0:
                color += 1
                continue
            
            nums[idx] = color
            idx += 1
            hashmap[color] -= 1
        

        
        
        