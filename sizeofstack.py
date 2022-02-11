def sizeofstack(start,auxiliar):
    sizeStart = 0

    while not start.isEmpty():
        x = start.pop()
        auxiliar.push(x)
        sizeStart += 1

    while not auxiliar.isEmpty():
        x = auxiliar.pop()
        start.push(x)

    return sizeStart