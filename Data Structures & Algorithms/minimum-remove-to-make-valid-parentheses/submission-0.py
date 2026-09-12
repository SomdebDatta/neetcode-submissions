class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op = []
        cl = []

        new_s = ''
        op_ct, cl_ct = 0, 0

        for idx in range(len(s)):
            if s[idx] == '(':
                op_ct += 1
            if s[idx] == ')':
                if cl_ct == op_ct:
                    continue
                else:
                    cl_ct += 1
            new_s += s[idx]
        
        s = new_s

        for idx, ch in enumerate(s):
            if ch == '(':
                op.append(idx)
            elif ch == ')':
                cl.append(idx)

        if len(op) == len(cl):
            return s
        
        to_remove = 0
        remove_op = 0
        remove_cl = 0
        if len(op) > len(cl):
            remove_op = len(op) - len(cl)
        else:
            remove_cl = len(cl) - len(op)
        
        if remove_op > 0:
            to_remove = remove_op
            remove_char = '('
        else:
            to_remove = remove_cl
            remove_char = ')'
        
        ans = ''
        removed = 0

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == remove_char and removed < to_remove:
                removed += 1
                continue
            ans = s[idx] + ans
        
        return ans
