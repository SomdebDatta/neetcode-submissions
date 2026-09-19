class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_idx = 0

        for i in range(1, len(arr)):
            if abs(x - arr[i]) < abs(arr[closest_idx] - x):
                closest_idx = i
                
        l, r = closest_idx - 1, closest_idx + 1
        ans = deque([arr[closest_idx]])

        while len(ans) < k:
            if l >= 0 and r < len(arr):
                if abs(arr[l] - x) > abs(arr[r] - x):
                    ans.append(arr[r])
                    r += 1
                else:
                    ans.appendleft(arr[l])
                    l -= 1
            elif l >= 0:
                ans.appendleft(arr[l])
                l -= 1
            elif r < len(arr):
                ans.append(arr[r])
                r += 1
        
        return list(ans)
                
