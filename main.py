from ExpressionEvaluator import ExpressionEvaluator

if __name__ == '__main__':
    tokens = ["4", "+", "3", "*", "(", "6", "-", "4", "!", ")"]
    ExpressionEvaluator.to_postfix(tokens)
