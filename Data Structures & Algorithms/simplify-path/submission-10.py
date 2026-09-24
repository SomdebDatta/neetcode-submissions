class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [d for d in path.split('/') if d not in ('', '.')]
        ans = []

        for idx, d in enumerate(directories):
            if d == '..':
                if idx > 0 and ans:
                    ans.pop()
                continue
            ans.append(d)

        return '/' + '/'.join(ans)