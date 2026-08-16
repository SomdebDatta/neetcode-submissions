class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for word in strs:
            encoded += str(len(word)) + 'N' + word
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []

        while i < len(s):
            j = i
            while j < len(s) and s[j] != 'N':
                j += 1
            ct = int(s[i:j])
            
            ans.append(s[j + 1: j + 1 + ct])
            i = j + 1 + ct
        return ans