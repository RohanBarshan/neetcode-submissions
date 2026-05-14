class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:                       #### if the stack is empty
            self.minstack.append(val)
        else:
            current_min = self.minstack[-1]
            get_min = min(val, current_min) 
            self.minstack.append(get_min)      


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]