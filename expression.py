import lexer
import reverse_polish_notation

class expression():
    def __init__(self,env={}):
        self.env = env


    def value(self,string):
        x = lexer.lexer(string)
        y = reverse_polish_notation.polish_notation_conversor(x)
        result = reverse_polish_notation.reverse_polish_notation_solver(y)
        return result

