import calculator

class inputfake():
    def __init__(self):
        self.inputlist = ["1"]
        self.outputlist = []

    def print(self, prompt):
        self.outputlist.append(prompt)

    def input(self,prompt):
        return self.inputlist.pop()

def test_main_number():
    x = inputfake()
    calculator.main(x)
    assert x.outputlist[0] == "1"

#def test_main_math():
    #x = input()
