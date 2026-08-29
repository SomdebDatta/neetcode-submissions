class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [item for item in path.split('/') if item not in ('', '.')]
        ans = []

        for directory in stack:
            if directory == '..':
                if ans:
                    ans.pop()
                continue
            ans.append(directory)

        return '/' + '/'.join(ans)