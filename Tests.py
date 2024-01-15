import pytest
from ExpressionEvaluator import ExpressionEvaluator

# Test cases
valid_test_cases = [
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
    ("(-3-(-(-3)))", -6)
]


@pytest.mark.parametrize("expression, expected", valid_test_cases)
def test_calculator(expression, expected):
    try:
        tokens = ExpressionEvaluator.tokenize(expression)
        ExpressionEvaluator.validate(tokens)
        result = ExpressionEvaluator.to_postfix(tokens)
        actual = ExpressionEvaluator.evaluate_postfix(result)
        print(f"Expression: '{expression}'")
        print(f"Expected result: '{expected}'")
        print(f"Actual result: '{actual}'")
        assert actual == expected
    except (SyntaxError, TypeError) as e:
        pytest.fail(f"Test failed with error: {e}")
