class FreqStack:

    def __init__(self):
        self.maxCount = 0
        self.num_to_count = defaultdict(int)
        self.count_to_num = defaultdict(list)

    def push(self, val: int) -> None:
        self.num_to_count[val] += 1
        self.maxCount = max(self.maxCount, self.num_to_count[val])
        self.count_to_num[self.num_to_count[val]].append(val)

    def pop(self) -> int:
        res = self.count_to_num[self.maxCount].pop()
        self.num_to_count[res] -= 1
        if not self.count_to_num[self.maxCount]:
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()