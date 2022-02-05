import stack

def test_isEmpty():
    assert stack.stack().isEmpty()

def test_push():
    x = stack.stack()
    x.push(1)
    assert not x.isEmpty()

def test_push_and_pop():
    x = stack.stack()
    x.push(1)
    x.pop()
    assert x.isEmpty()

def test_value_pop():
    x = stack.stack()
    x.push(1)
    popReturn = x.pop()
    assert popReturn == 1

def test_top_same_value():
    x = stack.stack()
    x.push(1)
    topReturn = x.top()
    assert topReturn == 1

def test_top_is_not_Empty():
    x = stack.stack()
    x.push(1)
    x.top()
    assert not x.isEmpty()