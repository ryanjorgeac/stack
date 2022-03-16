import expression
import inputIO


def main(userIO):
    exp = expression.expression()
    question = userIO.input("Write a math expression: ")
    while question != "exit":
        result = exp.value(question)
        userIO.print(result)
        question = userIO.input("Write a math expression: ")

if __name__ == "__main__":
    main(inputIO.inputIO())