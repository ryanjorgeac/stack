import sizeofstack

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
    while not start.isEmpty():
        x = sizeofstack.sizeofstack(start, destination)
        transfer_enesimo(x, start, destination)
    return
