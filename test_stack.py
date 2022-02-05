import stack

def test_isEmpty():
    assert stack.stack().isEmpty()

def test_push():
    x = stack.stack()
    x.push(1)
    assert not x.isEmpty()