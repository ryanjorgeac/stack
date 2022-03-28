import queue

def test_queue_isEmpty():
    assert queue.queue().isEmpty()

def test_queue_enqueue():
    x = queue.queue()
    x.enqueue(1)
    assert not x.isEmpty()

def test_dequeue():
    x = queue.queue()
    x.enqueue(1)
    x.dequeue()
    assert x.isEmpty()

def test_peek():
    x = queue.queue()
    x.enqueue(40)
    x.enqueue(5)
    x.enqueue(3)
    firstValue = x.peek()
    assert firstValue == 40