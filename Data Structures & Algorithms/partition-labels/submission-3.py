class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Calc last index of each char
        last_index = {}

        for idx, ch in enumerate(s):
            last_index[ch] = idx
        
        end = 0
        ans = []
        curr_len = 0
        # Check if you've reached the last idx of any char - if so, append to ans
        for idx, ch in enumerate(s):
            curr_len += 1
            end = max(end, last_index[ch])

            if idx == end:
                ans.append(curr_len)
                curr_len = 0
        
        return ans 
