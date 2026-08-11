class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0
        total = 0
        ans = 0

        for r in range(len(arr)):
            total += arr[r]
            if r - l < k - 1:
                continue
            if total / k >= threshold:
                ans += 1
            
            total -= arr[l]
            l += 1
        
        # if total / k > threshold:
        #     ans += 1
        
        return ans
            
            
            