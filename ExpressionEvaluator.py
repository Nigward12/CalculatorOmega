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
        previous_char = None
        for char in expression:
            if char.isdigit() or char == ".":  # handling the conjoining of adjacent digits
                element += char  # or decimal point to one token
            else:
                if element:
                    if '-' in element:  # handling the tokenization adjacent negative signing of a number
                        count = element.count('-')  # (like ------3=3)
                        if count % 2 == 0:
                            element = element[count:]
                        else:
                            element = element[count - 1:]
                    tokens.append(element)
                    element = ""
                if char == '-' and previous_char is None or previous_char in "+-*/%$&^@~(":
                    element += "-"  # handling negative signing of a number
                elif char in "+-*/%$&!^@~()":
                    tokens.append(char)
                else:
                    raise ValueError(f"Invalid character '{char}' in input expression")
                previous_char = char
        if element:  # adding the last number in a case where
            tokens.append(element)  # the last token in the expression is a number
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
