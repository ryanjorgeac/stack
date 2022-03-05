import stack
import transfer

def polish_notation_conversor(lexer):
    stackout = stack.stack()
    stackope = stack.stack()
    x = lexer.getnext()
    while x[1] != "END_OF_INPUT":
        if x[1] == "NUMBER":
            stackout.push(x)

        elif x[1] == "OPERATOR":
            stackope.push(x)

        else:
            return stackout
        x = lexer.getnext()


    while not stackope.isEmpty():
        x = stackope.pop()
        stackout.push(x)

    transfer.reverse_stack(stackout)
    return stackout

def reverse_polish_notation_solver(stack_reversed):
    def add(num1,num2):
        return num1+num2

    def multiply(num1,num2):
        return num1*num2

    def subtract(num1,num2):
        return num1-num2

    def divide(num1,num2):
        return num1/num2

    operators = {"+":add,"*":multiply,"-":subtract,"/":divide}

    numbers = stack.stack()

    while not stack_reversed.isEmpty():
        x = stack_reversed.pop()
        if x[1] == "NUMBER":
            numbers.push(int(x[0]))

        else:
            firstNumber = numbers.pop()
            secondNumber = numbers.pop()
            operation = operators[x[0]](firstNumber,secondNumber)
            numbers.push(operation)

    result = numbers.pop()
    return result