import stack
import lexer
import transfer


def fnotation(lexer):
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