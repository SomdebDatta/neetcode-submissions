class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []


        def backtracking(idx, curr):
            if idx == len(digits):
                ans.append(''.join(curr))
                return

            for ch in hashmap[digits[idx]]:
                curr.append(ch)
                backtracking(idx + 1, curr)
                curr.pop()
        backtracking(0, [])

        return ans