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
    ("1####", 1)
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
    except (SyntaxError, TypeError, ZeroDivisionError) as e:
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
    # to check for EOF and KeyboardInterrupt Errors , run them in main
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
