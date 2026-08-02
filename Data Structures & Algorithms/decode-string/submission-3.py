class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # Collecting the string
                curr_str = ''
                while True:
                    ch = stack.pop()
                    if ch == '[':
                        break
                    curr_str = ch + curr_str
                # Collecting the iterations
                curr_num = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    curr_num = digit + curr_num
                    # print(curr_num)
                stack.append(curr_str * int(curr_num))
            
        
        return ''.join(stack)

                    