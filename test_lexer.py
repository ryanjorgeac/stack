import lexer

def test_lexer():
    x = lexer.lexer("")
    next = x.getnext()
    assert next == ("","END_OF_INPUT")

def test_lexer_number():
    x = lexer.lexer("1")
    next = x.getnext()
    assert next == ("1","NUMBER")

def test_lexer_operator_sum():
    x = lexer.lexer("+")
    next = x.getnext()
    assert next == ("+","OPERATOR")

def test_lexer_operator_sub():
    x = lexer.lexer("-")
    next = x.getnext()
    assert next == ("-","OPERATOR")

def test_lexer_operator_times():
    x = lexer.lexer("*")
    next = x.getnext()
    assert next == ("*","OPERATOR")

def test_lexer_operator_division():
    x = lexer.lexer("/")
    next = x.getnext()
    assert next == ("/","OPERATOR")

def test_simple_sum():
    x = lexer.lexer("1+2")
    next1 = x.getnext()
    next2 = x.getnext()
    next3 = x.getnext()
    assert next1 == ("1","NUMBER") and next2 == ("+","OPERATOR") and next3 == ("2","NUMBER")

def test_sum_and_times():
    x = lexer.lexer("12+*")
    next1 = x.getnext()
    next2 = x.getnext()
    next3 = x.getnext()
    assert next1 == ("12","NUMBER") and next2 == ("+","OPERATOR") and next3 == ("*","OPERATOR")

def test_white_spaces():
    x = lexer.lexer("     ")
    next = x.getnext()
    assert next == ("","END_OF_INPUT")

def test_only_operators():
    x = lexer.lexer("+-*/")
    next1 = x.getnext()
    next2 = x.getnext()
    next3 = x.getnext()
    next4 = x.getnext()
    assert next1 == ("+","OPERATOR") and next2 == ("-","OPERATOR") and next3 == ("*","OPERATOR") and next4 == ("/","OPERATOR")

def test_sequence_of_number():
    x = lexer.lexer("12 12")
    next1 = x.getnext()
    next2 = x.getnext()
    assert next1 == ("12","NUMBER") and next2 == ("12","NUMBER")

def test_numbers_operator_and_space():
    x = lexer.lexer("12 + 4 * 2")
    next1 = x.getnext()
    next2 = x.getnext()
    next3 = x.getnext()
    next4 = x.getnext()
    next5 = x.getnext()
    assert next1 == ("12","NUMBER") and next2 == ("+","OPERATOR") and next3 == ("4","NUMBER") and next4 == ("*","OPERATOR") and next5 == ("2","NUMBER")

def test_1_plus_2():
    x = lexer.lexer("1+2")
    x.getnext()
    x.getnext()
    x.getnext()
    next4 = x.getnext()
    assert next4 == ("","END_OF_INPUT")

def test_with_parentheses():
    x = lexer.lexer("(1+2)*2")
    x1 = x.getnext()
    x.getnext()
    x.getnext()
    x.getnext()
    x2 = x.getnext()
    x.getnext()
    x.getnext()
    assert x1 == ("(","LEFT_PARENTHESES") and x2 == (")","RIGHT_PARENTHESES")