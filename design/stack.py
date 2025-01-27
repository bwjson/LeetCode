class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> int:
        val = self.stack[-1].pop()
        return val

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not bool(self.stack)
    
