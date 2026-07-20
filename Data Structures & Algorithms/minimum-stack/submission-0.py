class MinStack:

    def __init__(self):
        self.my_list = []
        self.mini = []

    def push(self, val: int) -> None:
        self.my_list.append(val)
        self.mini.append(val if not self.mini or val < self.mini[-1] else self.mini[-1])

    def pop(self) -> None:
        self.my_list.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.my_list[-1]

    def getMin(self) -> int:
        return self.mini[-1]
