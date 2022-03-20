import stack
import transfer


def precedencia(operator):
    dicio = {"+":10,"*":8,"-":9,"/":8,"=":11}
    return dicio[operator]


def polish_notation_conversor(lexer):
    stackout = stack.stack()
    stackope = stack.stack()
    x = lexer.getnext()
    while x[1] != "END_OF_INPUT":
        if x[1] == "NUMBER" or x[1] == "VARIABLE":
            stackout.push(x)

        elif x[1] == "OPERATOR":
            if not stackope.isEmpty() and stackope.top()[1] == "OPERATOR":
                topOperator = stackope.top()
                opeValue = precedencia(topOperator[0])
                newOpeValue = precedencia(x[0])
                if opeValue < newOpeValue:
                    while not stackope.isEmpty():
                        y = stackope.pop()
                        stackout.push(y)
            stackope.push(x)


        elif x[1] == "LEFT_PARENTHESES":
            stackope.push(x)

        elif x[1] == "RIGHT_PARENTHESES":
            while stackope.top()[1] != "LEFT_PARENTHESES":
                y = stackope.pop()
                stackout.push(y)
            stackope.pop()

        else:
            return stackout
        x = lexer.getnext()


    while not stackope.isEmpty():
        x = stackope.pop()
        stackout.push(x)

    transfer.reverse_stack(stackout)
    return stackout

def reverse_polish_notation_solver(stack_reversed,env={}):
    def add(num1,num2):
        return num1+num2

    def multiply(num1,num2):
        return num1*num2

    def subtract(num1,num2):
        return num2-num1

    def divide(num1,num2):
        return num1/num2

    operators = {"+":add,"*":multiply,"-":subtract,"/":divide}

    numbers = stack.stack()

    while not stack_reversed.isEmpty():
        x = stack_reversed.pop()
        if x[1] == "NUMBER":
            numbers.push(int(x[0]))

        elif x[1] == "VARIABLE":
            numbers.push(env[x[0]])

        else:
            firstNumber = numbers.pop()
            secondNumber = numbers.pop()
            operation = operators[x[0]](firstNumber,secondNumber)
            numbers.push(operation)

    result = numbers.pop()
    return result