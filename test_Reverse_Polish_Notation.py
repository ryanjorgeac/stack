import lexer
import reverse_polish_notation
import stack
import queue

def test_reverse_polish_notation():
    x = lexer.lexer("1+2")
    y = reverse_polish_notation.polish_notation_conversor(x)
    dequeue1 = y.dequeue()
    dequeue2 = y.dequeue()
    dequeue3 = y.dequeue()
    assert dequeue1 == ("1","NUMBER") and dequeue2 == ("2","NUMBER") and dequeue3 == ("+","OPERATOR")

def test_reverse_polish_notation2():
    x = lexer.lexer("1+2*3")
    y = reverse_polish_notation.polish_notation_conversor(x)
    dequeue1 = y.dequeue()
    dequeue2 = y.dequeue()
    dequeue3 = y.dequeue()
    dequeue4 = y.dequeue()
    dequeue5 = y.dequeue()
    assert dequeue1 == ("1","NUMBER") and dequeue2 == ("2","NUMBER") and dequeue3 == ("3","NUMBER") and dequeue4 == ("*","OPERATOR") and dequeue5 == ("+","OPERATOR")

def test_reverse_polish_notation3():
    x = lexer.lexer("2*2+3")
    y = reverse_polish_notation.polish_notation_conversor(x)
    dequeue1 = y.dequeue()
    dequeue2 = y.dequeue()
    dequeue3 = y.dequeue()
    dequeue4 = y.dequeue()
    dequeue5 = y.dequeue()
    assert dequeue1 == ("2","NUMBER") and dequeue2 == ("2","NUMBER") and dequeue3 == ("*","OPERATOR") and dequeue4 == ("3","NUMBER") and dequeue5 == ("+","OPERATOR")

def test_reverse_polish_notation_with_parentheses():
    x = lexer.lexer("4*(5-3)")
    y = reverse_polish_notation.polish_notation_conversor(x)
    dequeue1 = y.dequeue()
    dequeue2 = y.dequeue()
    dequeue3 = y.dequeue()
    dequeue4 = y.dequeue()
    dequeue5 = y.dequeue()
    assert dequeue1 == ("4", "NUMBER") and dequeue2 == ("5", "NUMBER") and dequeue3 == ("3", "NUMBER") and dequeue4 == ("-", "OPERATOR") and dequeue5 == ("*", "OPERATOR")


def test_conversor_with_variable_on_lexer():
    x = lexer.lexer("batata*4")
    y = reverse_polish_notation.polish_notation_conversor(x)
    dequeue1 = y.dequeue()
    dequeue2 = y.dequeue()
    dequeue3 = y.dequeue()
    assert dequeue1 == ("batata","VARIABLE") and dequeue2 == ("4","NUMBER") and dequeue3 == ("*","OPERATOR")


def test_conversor_with_operator_equals():
    x = lexer.lexer("batata=4")
    y = reverse_polish_notation.polish_notation_conversor(x)
    pop1 = y.dequeue()
    pop2 = y.dequeue()
    pop3 = y.dequeue()
    assert pop1 == ("batata", "VARIABLE") and pop2 == ("4", "NUMBER") and pop3 == ("=", "OPERATOR")

def test_conversor_with_equals_and_more_operators():
    x = lexer.lexer("batata=4*10+5")
    y = reverse_polish_notation.polish_notation_conversor(x)
    pop1 = y.dequeue()
    pop2 = y.dequeue()
    pop3 = y.dequeue()
    pop4 = y.dequeue()
    pop5 = y.dequeue()
    pop6 = y.dequeue()
    pop7 = y.dequeue()
    assert pop1 == ("batata","VARIABLE") and pop2 == ("4","NUMBER") and pop3 == ("10","NUMBER") and pop4 == ("*","OPERATOR") and pop5 == ("5","NUMBER") and pop6 == ("+","OPERATOR") and pop7 == ("=","OPERATOR")

def test_polish_notation_sum():
    x = queue.queue()
    x.enqueue(("1", "NUMBER"))
    x.enqueue(("2", "NUMBER"))
    x.enqueue(("+", "OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 3

def test_polish_notation_multiply_and_sum():
    x = queue.queue()
    x.enqueue(("1", "NUMBER"))
    x.enqueue(("2", "NUMBER"))
    x.enqueue(("3", "NUMBER"))
    x.enqueue(("*", "OPERATOR"))
    x.enqueue(("+", "OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 7

def test_polish_notation_minus():
    x = queue.queue()
    x.enqueue(("4", "NUMBER"))
    x.enqueue(("2", "NUMBER"))
    x.enqueue(("-", "OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 2

def test_polish_notation_minus2():
    x = queue.queue()
    x.enqueue(("40", "NUMBER"))
    x.enqueue(("15", "NUMBER"))
    x.enqueue(("-","OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 25

def test_polish_notation_division():
    x = queue.queue()
    x.enqueue(("6","NUMBER"))
    x.enqueue(("2","NUMBER"))
    x.enqueue(("/","OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 3

def test_polish_notation_division2():
    x = queue.queue()
    x.enqueue(("81", "NUMBER"))
    x.enqueue(("9", "NUMBER"))
    x.enqueue(("/","OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 9

def test_polish_notation_with_subtraction():
    x = queue.queue()
    x.enqueue(("4", "NUMBER"))
    x.enqueue(("5", "NUMBER"))
    x.enqueue(("-", "OPERATOR"))
    x.enqueue(("3", "NUMBER"))
    x.enqueue(("+","OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 2

def test_solver_with_variable():
    env = {"batata":42}
    x = queue.queue()
    x.enqueue(("batata", "VARIABLE"))
    x.enqueue(("4", "NUMBER"))
    x.enqueue(("+","OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x,env)
    assert z == 46


def test_solver_with_error_on_variables():
    env = {}
    x = queue.queue()
    x.enqueue(("x", "VARIABLE"))
    x.enqueue(("3", "NUMBER"))
    x.enqueue(("=","OPERATOR"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x,env)
    assert z == None

def test_solver_with_error_on_variables_2():
    env = {}
    x = queue.queue()
    x.enqueue(("x", "VARIABLE"))
    x.enqueue(("3", "NUMBER"))
    x.enqueue(("=", "OPERATOR"))
    reverse_polish_notation.reverse_polish_notation_solver(x, env)
    assert env["x"] == 3

if __name__ == "__main__":
    test_polish_notation_sum()