class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # Collecting the string
                curr_str = ''
                while stack[-1] != '[':
                    curr_str = stack.pop() + curr_str
                
                # Removing the [
                stack.pop()
                curr_num = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    curr_num = digit + curr_num
                stack.append(int(curr_num) * curr_str)
        
        return ''.join(stack)
                
                