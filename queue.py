class queue():
    def __init__(self):
        self.l = []

    def isEmpty(self):
        return len(self.l) == 0

    def enqueue(self,value):
        self.l.append(value)

    def dequeue(self):
        return self.l.pop(0)

    def peek(self):
        return self.l[0]