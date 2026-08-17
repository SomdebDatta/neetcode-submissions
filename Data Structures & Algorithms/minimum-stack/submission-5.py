class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        self.mini = min(self.mini, val)
        self.min_stack.append(self.mini)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.mini = self.min_stack[-1] if self.min_stack else float('inf')
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.min_stack)
        return self.mini
