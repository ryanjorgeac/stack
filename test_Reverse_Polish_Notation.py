import lexer
import reverse_polish_notation
import stack


def test_reverse_polish_notation():
    x = lexer.lexer("1+2")
    y = reverse_polish_notation.polish_notation_conversor(x)
    pop1 = y.pop()
    pop2 = y.pop()
    pop3 = y.pop()
    assert pop1 == ("1","NUMBER") and pop2 == ("2","NUMBER") and pop3 == ("+","OPERATOR")

def test_reverse_polish_notation2():
    x = lexer.lexer("1+2*3")
    y = reverse_polish_notation.polish_notation_conversor(x)
    pop1 = y.pop()
    pop2 = y.pop()
    pop3 = y.pop()
    pop4 = y.pop()
    pop5 = y.pop()
    assert pop1 == ("1","NUMBER") and pop2 == ("2","NUMBER") and pop3 == ("3","NUMBER") and pop4 == ("*","OPERATOR") and pop5 == ("+","OPERATOR")

def test_reverse_polish_notation3():
    x = lexer.lexer("2*2+3")
    y = reverse_polish_notation.polish_notation_conversor(x)
    pop1 = y.pop()
    pop2 = y.pop()
    pop3 = y.pop()
    pop4 = y.pop()
    pop5 = y.pop()
    assert pop1 == ("2","NUMBER") and pop2 == ("2","NUMBER") and pop3 == ("*","OPERATOR") and pop4 == ("3","NUMBER") and pop5 == ("+","OPERATOR")

def test_reverse_polish_notation_with_parentheses():
    x = lexer.lexer("4*(5-3)")
    y = reverse_polish_notation.polish_notation_conversor(x)
    pop1 = y.pop()
    pop2 = y.pop()
    pop3 = y.pop()
    pop4 = y.pop()
    pop5 = y.pop()
    assert pop1 == ("4", "NUMBER") and pop2 == ("5", "NUMBER") and pop3 == ("3", "NUMBER") and pop4 == ("-", "OPERATOR") and pop5 == ("*", "OPERATOR")


def test_polish_notation_sum():
    x = stack.stack()
    x.push(("+", "OPERATOR"))
    x.push(("2", "NUMBER"))
    x.push(("1", "NUMBER"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 3

def test_polish_notation_multiply_and_sum():
    x = stack.stack()
    x.push(("+","OPERATOR"))
    x.push(("*","OPERATOR"))
    x.push(("3","NUMBER"))
    x.push(("2","NUMBER"))
    x.push(("1","NUMBER"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 7

def test_polish_notation_minus():
    x = stack.stack()
    x.push(("-","OPERATOR"))
    x.push(("2","NUMBER"))
    x.push(("4","NUMBER"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 2

def test_polish_notation_minus2():
    x = stack.stack()
    x.push(("-","OPERATOR"))
    x.push(("15","NUMBER"))
    x.push(("40","NUMBER"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 25

def test_polish_notation_division():
    x = stack.stack()
    x.push(("/","OPERATOR"))
    x.push(("6","NUMBER"))
    x.push(("2","NUMBER"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 3

def test_polish_notation_division2():
    x = stack.stack()
    x.push(("/","OPERATOR"))
    x.push(("81","NUMBER"))
    x.push(("9","NUMBER"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 9

def test_polish_notation_with_subtraction():
    x = stack.stack()
    x.push(("+","OPERATOR"))
    x.push(("3","NUMBER"))
    x.push(("-","OPERATOR"))
    x.push(("5","NUMBER"))
    x.push(("4","NUMBER"))
    z = reverse_polish_notation.reverse_polish_notation_solver(x)
    assert z == 2


