class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        visited = set(deadends)
        q = deque()
        q.append(['0000', 0])

        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns

            for idx, num in enumerate(lock):
                # +1
                int_num = int(num)
                next_num = (int_num + 1 + 10) % 10
                next_lock = lock[:idx] + str(next_num) + lock[idx + 1:]
                if next_lock not in visited:
                    visited.add(next_lock)
                    q.append([next_lock, turns + 1])

                # -1
                int_num = int(num)
                next_num = (int_num - 1 + 10) % 10
                next_lock = lock[:idx] + str(next_num) + lock[idx + 1:]
                if next_lock not in visited:
                    visited.add(next_lock)
                    q.append([next_lock, turns + 1])
        
        return -1
        
