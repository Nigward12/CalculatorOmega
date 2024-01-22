import pytest
from ExpressionEvaluator import ExpressionEvaluator

# pytest file for checking the calculator for correct handling of valid expressions and their evaluation
# and for correct handling of Invalid expressions and the raising of correct errors with informative info
# about the cause of the error

valid_test_cases = [
    #  list of valid expressions and the result they should logically provide
    #  format : ("expression" , expected result)
    ("3 + 4 * 2", 11),
    ("2 ^ 3 + 1", 9),
    ("10 % 3 * 4", 4),
    ("6 / 2 - 3", 0),
    ("5@10 + 2", 9.5),
    ("2$5 * 3", 15),
    ("3&7 - 1", 2),
    ("4! / 2", 12),
    ("~123 + 5", -118),
    ("123# * 2", 12),
    ("---3 + 4", 1),
    ("2 ^ (3 + 1)", 16),
    ("(5@10) * 2", 15),
    ("(3&7) ^ 2", 9),
    ("4 * (2 + 3)", 20),
    ("4+-(3^2)", -5),
    ("---3!", -6),
    ("~-4", 4),
    ("(-3-(-(-3)))", -6),
    ("3 * 4 + 2 ^ 2", 16),
    ("(10 % 3) * (4 + 2)", 6),
    ("(6 / (2 - 3)) + 5", -1),
    ("5@10 * 2$5", 37.5),
    ("3&7 - 1 * 4!", -21),
    ("~123 * 2 - 5", -251),
    ("(123# + 3) ^ 2", 81),
    ("---(3 + 4)", -7),
    ("5   5", 55),
    ("4!!##", 9),
    ("~-4!", 24),
    ("1####", 1),
    ("-3^2", -9),
    ("5  .   5", 5.5),
    ("~-4!#&7$4@6%4^2+(-4*3)", -8),
    ("2 - - - 3", -1),
    # now the long ones
    ("6!+4*(5@3)+2*(8-3)", 746),
    ("(-4)^2-7$3+10*(2+3)", 59),
    ("8%3+(10&2)*4+(9-2)*5", 45),
    ("5*(4+3@2)-~(-6)+12/6", 28.5),
    ("10/(2+3)*(7-5$2)+(1+2)", 7),
    ("9+8*(6@4)/2+14-3*2", 37),
    ("(4+5*3-2)@(6+7/3)+10/2", 17.6666666667),
    ("3^(4%2)+7&5+(6+4)/2", 3**(4 % 2) + min(7, 5) + (6 + 4) / 2),
    ("12/(6/3)+(5*4)@2+3*7", 12 / (6 / 3) + ((5 * 4 + 2) / 2) + 3 * 7),
    ("18%(7-5)-10&(8/2)+7*3", 18 % (7 - 5) - min(10, 8 / 2) + 7 * 3),
    ("4*(3+2)$(5^2)+2-3*5", 4*max((3+2), (5**2)) + 2 - 3 * 5),
    ("20-(3*4)&(6/2)+5*(4+3)", 20 - min((3*4), (6/2)) + 5 * (4 + 3)),
    ("15/(5%3)+7@(4*2)+3^2", 15 / (5 % 3) + ((7 + 4 * 2) / 2) + 3**2),
    ("9+8-7*6/5%4+10*(3-1)", 9 + (8 - 7 * 6 / (5 % 4)) + 10 * (3 - 1)),
    ("18-(7$5)+4*3+5/2-6*7", 18 - max(7, 5) + 4 * 3 + 5 / 2 - 6 * 7),
    ("6@(4-2)*(3+5)+9-4/2", (6 + (4 - 2)) / 2 * (3 + 5) + 9 - 4 / 2),
    ("12/(6/3)-10%(5*2)+14/7", 12 / (6 / 3) - 10 % (5 * 2) + 14 / 7),
    ("5^(4@2)-7%3+8*(2+5)", 5**((4 + 2) / 2) - 7 % 3 + 8 * (2 + 5)),
    ("20&(10/2)+(3*4)$5+7-3", min(20, 10 / 2) + max(3 * 4, 5) + 7 - 3),
    ("9%(8-6)-7$(5/2)+6*4-2", 9 % (8 - 6) - max(7, 5 / 2) + 6 * 4 - 2),
]


@pytest.mark.parametrize("expression, expected", valid_test_cases)
def test_calculator_valids(expression, expected):
    # method will try to run each of the expressions through calculation
    # a test will be considered as passed if the result matched the expected result
    # a test will fail if the result doesn't match the expected result or an error was raised
    try:
        tokens = ExpressionEvaluator.tokenize(expression)
        ExpressionEvaluator.validate(tokens)
        result = ExpressionEvaluator.to_postfix(tokens)
        actual = ExpressionEvaluator.evaluate_postfix(result)
        print(f"Expression: '{expression}'")
        print(f"Expected result: '{expected}'")
        print(f"Actual result: '{actual}'")
        assert actual == expected
    except (SyntaxError, TypeError, ZeroDivisionError, ValueError) as e:
        pytest.fail(f"Test failed with error: {e}")


invalid_test_cases = [
    #  list of invalid expressions and the Error they should logically provide
    #  format : ("expression" , expected error)
    ("!4", SyntaxError),
    ("-", SyntaxError),
    ("-~3", SyntaxError),
    ("4**", SyntaxError),
    ("()", SyntaxError),
    (" ", SyntaxError),
    ("(4))", SyntaxError),
    ("4+-3!", TypeError),
    ("4/0", ZeroDivisionError),
    ("5*(3)4", SyntaxError),
    ("5+", SyntaxError),
    ("-4(4+3)", SyntaxError),
    ("(4))", SyntaxError),
    ("3..4", SyntaxError),
    (".", SyntaxError),
    ("", SyntaxError),
    ("(4))", SyntaxError),
    ("a*43", SyntaxError),
    ("  ", SyntaxError),  # \t
    ("~~4", SyntaxError),
    ("(4))", SyntaxError),
    ("4+5-(3)(", SyntaxError),
    ("4+5$", SyntaxError),
    ("4+4&*3", SyntaxError),
    ("4+5$", SyntaxError),
    ("~4!", TypeError),
    ("1!!!!2", SyntaxError),
    ("3!~2", SyntaxError),
    ("3!!!3", SyntaxError),
    ("2~2", SyntaxError),
    ("~--3!", TypeError),
    ("--~--3", SyntaxError),
    ("~--~-3", SyntaxError),
    ("2 - - 3!", TypeError),
    ("0^-1", ZeroDivisionError),
    ("~2^0.5", ValueError)
    # to check for EOF Error , run in main
]


@pytest.mark.parametrize("expression, expected_error", invalid_test_cases)
def test_calculator_invalids(expression, expected_error):
    # method will try to run each of the expressions through calculation
    # a test will be considered as passed if the calculation process correctly raised an informative error
    # on the invalid expression
    # a test will fail if no error or an unexpected error was raised
    try:
        tokens = ExpressionEvaluator.tokenize(expression)
        ExpressionEvaluator.validate(tokens)
        result = ExpressionEvaluator.to_postfix(tokens)
        ExpressionEvaluator.evaluate_postfix(result)
        pytest.fail(f"Expression: '{expression}' - should have raised an error but did not.")
    except expected_error:
        print(f"Expression: '{expression}' - correctly raised an error")
    except Exception as e:
        pytest.fail(f"Expression: '{expression}' - raised an unexpected error: {e}")
