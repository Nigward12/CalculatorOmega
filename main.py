from ExpressionEvaluator import ExpressionEvaluator

if __name__ == '__main__':
    expression = "(4+-----5*(4^2!)*2)^2!!#"  # problem with - in tokenization , also need to allow stacking operators in validation
    tokens = ExpressionEvaluator.tokenize(expression)
    ExpressionEvaluator.validate(tokens)
    ExpressionEvaluator.to_postfix(tokens)
