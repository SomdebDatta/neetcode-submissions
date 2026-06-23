class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = str()
        for word in strs:
            ans = ans + str(len(word)) + "#" + word
        return ans

    def decode(self, s: str) -> List[str]:
        num_start = 0
        i = 0
        ans = list()
        word = str()
        while i < len(s):

            if s[i] != "#":
                i += 1
                continue
            num_len = int(s[num_start:i])
            word = s[i + 1 : i + 1 + num_len]
            print(word)
            ans.append(word)
            num_start = i + 1 + num_len 
            i = num_start + 1
        return ans