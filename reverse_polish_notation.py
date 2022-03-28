import stack
import queue

def precedencia(operator):
    dicio = {"+":10,"*":8,"-":9,"/":8,"=":11}
    return dicio[operator]


def polish_notation_conversor(lexer):
    queueout = queue.queue()
    stackope = stack.stack()
    x = lexer.getnext()
    while x[1] != "END_OF_INPUT":
        if x[1] == "NUMBER" or x[1] == "VARIABLE":
            queueout.enqueue(x)

        elif x[1] == "OPERATOR":
            while not stackope.isEmpty() and stackope.top()[1] == "OPERATOR":
                topOperator = stackope.top()
                topOpeValue = precedencia(topOperator[0])
                xOpeValue = precedencia(x[0])
                if topOpeValue < xOpeValue:
                    y = stackope.pop()
                    queueout.enqueue(y)
                else:
                    break
            stackope.push(x)


        elif x[1] == "LEFT_PARENTHESES":
            stackope.push(x)

        elif x[1] == "RIGHT_PARENTHESES":
            while stackope.top()[1] != "LEFT_PARENTHESES":
                y = stackope.pop()
                queueout.enqueue(y)
            stackope.pop()

        else:
            return queueout
        x = lexer.getnext()


    while not stackope.isEmpty():
        x = stackope.pop()
        queueout.enqueue(x)

    return queueout

def reverse_polish_notation_solver(newQueue,env={}):
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

    while not newQueue.isEmpty():
        x = newQueue.dequeue()
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