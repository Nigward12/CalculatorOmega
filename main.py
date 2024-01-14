from ExpressionEvaluator import ExpressionEvaluator

if __name__ == '__main__':
    #  receives a string from the input , the string goes through separation to tokens
    #  and validation of syntax , if the expression is valid , it will be converted to
    #  postfix and calculated according to the shunting yard algorithm
    #  the program will keep receiving new inputs until the input is "done"
    expression = input("Enter a valid infix expression for calculation , enter \"done\" to exit: ")
    while not expression == "done":
        try:
            tokens = ExpressionEvaluator.tokenize(expression)
            ExpressionEvaluator.validate(tokens)
            result = ExpressionEvaluator.to_postfix(tokens)
            print(f"{ExpressionEvaluator.evaluate_postfix(result)}")
        except (SyntaxError, TypeError) as e:
            print(f"{e}")
        expression = input("Enter a valid infix expression for calculation , enter \"done\" to exit: ")
