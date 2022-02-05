class stack:
    def __init__(self):
        self.l = []

    def isEmpty(self):
        return len(self.l) == 0

    def push(self,value):
        self.l.append(value)
