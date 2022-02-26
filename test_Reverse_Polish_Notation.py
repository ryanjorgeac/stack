import lexer
import reverse_polish_notation
import stack


def test_reverse_polish_notation():
    x = lexer.lexer("1+2")
    y = reverse_polish_notation.fnotation(x)
    pop1 = y.pop()
    pop2 = y.pop()
    pop3 = y.pop()
    assert pop1 == ("1","NUMBER") and pop2 == ("2","NUMBER") and pop3 == ("+","OPERATOR")

def test_polish_notation_calculated():
    x = stack.stack()
    x.push(("+", "OPERATOR"))
    x.push(("2", "NUMBER"))
    x.push(("1", "NUMBER"))
    z = reverse_polish_notation.fnotationSolver(x)
    assert z == 3

def test_polish_notation_calculated2():
    x = stack.stack()
    x.push(("+","OPERATOR"))
    x.push(("*","OPERATOR"))
    x.push(("3","NUMBER"))
    x.push(("2","NUMBER"))
    x.push(("1","NUMBER"))
    z = reverse_polish_notation.fnotationSolver(x)
    assert z == 7