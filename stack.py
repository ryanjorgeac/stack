class stack():
    def __init__(self):
        self.l = []

    def isEmpty(self):
        return len(self.l) == 0

    def push(self,value):
        self.l.append(value)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def __str__(self):
        stackStr = ""
        for i in range(len(self.l)-1,-1,-1):
            stackStr+= f"{self.l[i]} "
        return stackStr