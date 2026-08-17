class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            if not stack:
                if bracket in hashmap.keys():
                    return False
                stack.append(bracket)
                continue
            
            if bracket in hashmap.keys():
                if hashmap[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)
            
        if stack:
            return False
        return True