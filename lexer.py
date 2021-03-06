import string

class lexer():
    #s -> string
    def __init__(self,s):
        self.s = s
        self.state = 0
        self.digits = ["0","1","2","3","4","5","6","7","8","9"]
        self.operators = ["+","-","*","/","="]
        self.left_parentheses = ["("]
        self.right_parentheses = [")"]
        self.letters = string.ascii_letters


    def getnext(self):
        aux = ""
        final_index = 0
        for index,i in enumerate(self.s):
            final_index = index
            if i in self.digits and self.state == 0:
                self.state = 1
                aux = i

            elif i in self.digits and self.state == 1:
                aux += i


            elif i in self.operators and self.state == 0:
                aux = i
                self.state = 2

            elif i in self.left_parentheses and self.state == 0:
                aux = i
                self.state = 3

            elif i in self.right_parentheses and self.state == 0:
                aux = i
                self.state = 4

            elif i in self.letters and self.state == 0:
                aux = i
                self.state = 5

            elif i in self.letters and self.state == 5:
                aux += i

            elif i in self.digits and self.state == 5:
                aux += i


            elif i == " " and self.state == 0:
                continue

            else:
                break

        rc = ()

        if self.state == 0:
            rc = (aux,"END_OF_INPUT")

        elif self.state == 1:
            rc = (aux,"NUMBER")

        elif self.state == 2:
            rc = (aux,"OPERATOR")

        elif self.state == 3:
            rc = (aux,"LEFT_PARENTHESES")

        elif self.state == 4:
            rc = (aux,"RIGHT_PARENTHESES")

        elif self.state == 5:
            rc = (aux,"VARIABLE")


        self.state = 0

        if final_index != 0:
            self.s = self.s[final_index:]

        else:
            self.s = ""

        return rc