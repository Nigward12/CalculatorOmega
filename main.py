from ExpressionEvaluator import ExpressionEvaluator

if __name__ == '__main__':
    #  receives a string from the input , the string goes through separation to tokens
    #  and validation of syntax , if the expression is valid , it will be converted to
    #  postfix and calculated according to the shunting yard algorithm
    #  the program will keep receiving new inputs until the input is "done"
    try:
        expression = input("Enter a valid infix expression for calculation , enter \"done\" to exit: ")
    except EOFError as e:
        print(f"{e}")
        exit(0)
    while not expression == "done":
        try:
            tokens = ExpressionEvaluator.tokenize(expression)
            ExpressionEvaluator.validate(tokens)
            result = ExpressionEvaluator.to_postfix(tokens)
            print(f"{ExpressionEvaluator.evaluate_postfix(result)}")
        except (SyntaxError, TypeError, ZeroDivisionError, ValueError) as e:
            print(f"{e}")
        try:
            expression = input("Enter a valid infix expression for calculation , enter \"done\" to exit: ")
        except EOFError as e:
            print(f"{e}")
            exit(0)
