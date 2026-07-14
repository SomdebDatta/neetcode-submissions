class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)

        for task in tasks:
            counter[task] += 1
        
        maxHeap = [-val for val in counter.values()]

        heapq.heapify(maxHeap)

        q = deque()
        time = 0


        while q or maxHeap:
            time += 1

            if maxHeap:
                curr = heapq.heappop(maxHeap)
                if curr + 1:
                    q.append([curr + 1, time + n])
                else:
                    print(f'curr - {curr}')
            else:
                time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
            