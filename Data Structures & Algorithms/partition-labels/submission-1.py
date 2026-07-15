class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Calc total freq
        total_freq = defaultdict(int)
        for ch in s:
            total_freq[ch] += 1
        
        curr_freq = defaultdict(int)
        curr_str = ''
        ans = []

        # Check if curr_freq == total_freq
        def check(curr_freq) -> bool:
            if not curr_freq:
                return False
            for key in curr_freq:
                if curr_freq[key] != total_freq[key]:
                    return False
            return True
        
        for idx, ch in enumerate(s):
            curr_freq[ch] += 1
            curr_str += ch
            if check(curr_freq):
                print(curr_str)
                ans.append(len(curr_str))
                curr_freq = defaultdict(int)
                curr_str = ''
        
        return ans