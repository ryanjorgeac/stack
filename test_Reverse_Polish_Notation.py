import lexer
import reverse_polish_notation

def test_reverse_polish_notation():
    x = lexer.lexer("1+2")
    y = reverse_polish_notation.fnotation(x)
    pop1 = y.pop()
    pop2 = y.pop()
    pop3 = y.pop()
    assert pop1 == ("1","NUMBER") and pop2 == ("2","NUMBER") and pop3 == ("+","OPERATOR")