import stack
import sizeofstack
import transfer

def test_size_of_stack1():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    x = sizeofstack.sizeofstack(stack1,stack2)
    assert x == 5

def test_stack2_is_empty():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    sizeofstack.sizeofstack(stack1, stack2)
    assert stack2.isEmpty()

def test_stack1_is_not_empty():
    stack1 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    assert not stack1.isEmpty()

def test_stack1_is_the_same():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    sizeofstack.sizeofstack(stack1,stack2)
    x1 = stack1.pop()
    x2 = stack1.pop()
    x3 = stack1.pop()
    x4 = stack1.pop()
    x5 = stack1.pop()
    assert x1 == 5 and x2 == 4 and x3 == 3 and x4 == 2 and x5 == 1

def test_transfer_enesimo():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack2.push(5)
    stack2.push(10)
    transfer.transfer_enesimo(2,stack1,stack2)
    assert stack2.top() == 2

def test_transfer_enesimo_values_of_first_stack():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack2.push(5)
    stack2.push(10)
    transfer.transfer_enesimo(2, stack1, stack2)
    x1 = stack1.pop()
    x2 = stack1.pop()
    assert x1 == 3 and x2 == 1

def test_if_stack1_is_empty():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    transfer.transfer(stack1,stack2)
    assert stack1.isEmpty()

def test_if_stack2_is_not_empty():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    transfer(stack1, stack2)
    assert not stack2.isEmpty()

def test_if_stack2_is_reversed():
    stack1 = stack.stack()
    stack2 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    transfer(stack1, stack2)
    x1 = stack2.pop()
    x2 = stack2.pop()
    x3 = stack2.pop()
    x4 = stack2.pop()
    x5 = stack2.pop()
    assert x1 == 5 and x2 == 4 and x3 == 3 and x4 == 2 and x5 == 1

def test_reverse_stack():
    stack1 = stack.stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    reverse_stack(stack1)
    x1 = stack1.pop()
    x2 = stack1.pop()
    x3 = stack1.pop()
    assert x1 == 1 and x2 == 2 and x3 == 3