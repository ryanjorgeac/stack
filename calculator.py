import lexer
import reverse_polish_notation


def is_an_int(x):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    for i in x:
        if not i in digits:
            return False
    return True


def main(userIO):
    question = userIO.input("Write a number or an expression: ")
    x = lexer.lexer(question)
    y = reverse_polish_notation.polish_notation_conversor(x)
    result = reverse_polish_notation.reverse_polish_notation_solver(y)
    userIO.print(result)


class inputIO():
    def input(self,prompt):
        return input(prompt)

    def print(self,prompt):
        print(prompt)


if __name__ == "__main__":
    main(inputIO())