class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [item for item in path.split('/') if item not in ('', '.')]
        print(stack)
        ans = []

        for directory in stack:
            if directory == '..':
                if ans:
                    ans.pop()
                continue
            ans.append(directory)
        
        print(ans)

        return '/' + '/'.join(ans)