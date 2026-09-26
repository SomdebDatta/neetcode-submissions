class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_ct = 0
        even_ct = 0
        ans = 0
        prefix_sum = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum % 2:
                ans += 1 + even_ct
                odd_ct += 1
            else:
                ans += odd_ct
                even_ct += 1
        
        return ans