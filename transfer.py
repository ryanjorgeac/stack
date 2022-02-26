import sizeofstack
import stack

def transfer_enesimo(n, p1, p2):
    for i in range(n-1):
        y = p1.pop()
        p2.push(y)
    x = p1.pop()
    for i in range(n - 1):
        y = p2.pop()
        p1.push(y)
    p2.push(x)
    return

def transfer(start, destination):
    aux = stack.stack()
    while not start.isEmpty():
        x = sizeofstack.sizeofstack(start, aux)
        transfer_enesimo(x, start, destination)
    return

def reverse_stack(p1):
    x = p1
    y = stack.stack()
    transfer(x,y)
    aux = stack.stack()
    sizey = sizeofstack.sizeofstack(y,aux)
    for i in range(sizey):
        z = y.pop()
        x.push(z)
    return x