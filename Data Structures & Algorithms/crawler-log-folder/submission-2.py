class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            match log:
                case './':
                    continue
                case '../':
                    if depth > 0:
                        depth -= 1
                case _:
                    depth += 1
        return depth