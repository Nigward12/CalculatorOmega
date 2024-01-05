class ExpressionEvaluator(object):
    # this class is a service class is a service class that contains
    # methods to handle the evaluation of the input string
    # and the calculation process of the string
    @staticmethod
    def tokenize(expression):
        # this method handles the tokenization of the input expression
        # into separate expressions each representing a number, operator
        # or parenthesis
        # it uses a list to hold all the tokens and returns it
        tokens = []
        element = ""
        for char in expression:
            if char.isdigit() or char == ".":  # handling the conjoining of adjacent digits
                element += char  # or decimal point to one token
            else:
                if element:
                    tokens.append(element)
                    element = ""
                if char in "+-*/%$&!^@~()":
                    tokens.append(char)
        if element:
            tokens.append(element)
        return tokens

    @staticmethod
    def validate(tokens):
        pass

    @staticmethod
    def to_postfix(tokens):
        pass

    @staticmethod
    def evaluate_postfix(postfix_tokens):
        pass
