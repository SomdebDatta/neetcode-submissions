class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = str()
        for word in strs:
            ans += str(len(word)) + '#' + word
        return ans

    def decode(self, s: str) -> List[str]:
        ans = list()
        word_start = 0
        i = 0

        while i < len(s):
            if s[i] != '#':
                i += 1
                continue
            
            word_len = int(s[word_start: i])
            word = s[i+1: i+1+word_len]
            ans.append(word)
            word_start, i = i+word_len+1, i+word_len+1
            print(ans)
        return ans