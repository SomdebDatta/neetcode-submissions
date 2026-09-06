class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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


        ans = [""]

        for digit in digits:
            new_ans = []
            for word in ans:
                for letter in hashmap[digit]:
                    new_ans.append(word + letter)
            ans = new_ans
        
        return ans