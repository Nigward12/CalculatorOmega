from OperatorFactory import OperatorFactory


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
        if not expression.strip():  # check for an input empty of relevant context
            raise SyntaxError("expression is empty")
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
                        element = element[count:]
                        if count % 2 != 0:
                            tokens.append('-')  # adding the negative sign as a separate token
                    tokens.append(element)
                    element = ""
                if char == '-' and (previous_char is None or previous_char in "+-*/%$&^@~("):
                    element += "-"  # handling negative signing of a number
                elif char in "+-*/%$&!^@~()":
                    tokens.append(char)
                else:
                    raise SyntaxError(f"Invalid character '{char}' in input expression")
                previous_char = char
        if element:  # adding the last number in a case where
            tokens.append(element)  # the last token in the expression is a number
        return tokens

    @staticmethod
    def validate(tokens):
        if not tokens:
            raise SyntaxError("The expression is empty.")
        factory = OperatorFactory()
        ExpressionEvaluator._validate_first_token(tokens)
        ExpressionEvaluator._validate_parenthesis(tokens)
        ExpressionEvaluator._validate_operators(tokens, factory)

    @staticmethod
    def _validate_first_token(tokens):
        #  private method of ExpressionEvaluator , used by validate()
        #  method to check the validity of the first token in the expression
        #  first token cant be an operator unless it's a negative sign or tilda with a number after
        if (tokens[0] in "+*/%$&!^@)" or
                (tokens[0] in '-~' and not isinstance(tokens[1], (int, float)))):
            raise SyntaxError(f"'{tokens[0]}' can't be the first character in the expression")

    @staticmethod
    def _validate_parenthesis(tokens):
        #  private method of ExpressionEvaluator , used by validate()
        #  method to check the validity of all the parenthesis in the expression
        #  checks that each opening parenthesis has closing ones and that there are no
        #  more parenthesis of one kind than the other , also checks for empty parenthesis
        open_parenthesis_cnt = 0
        for i in range(0, len(tokens)):
            if tokens[i] == '(':
                if (tokens[i + 1]) == ')':
                    raise SyntaxError(f"at {i + 1}'th-{i + 2}'th characters, '()', empty parenthesis are not allowed")
                open_parenthesis_cnt += 1
            elif tokens[i] == ')':
                open_parenthesis_cnt -= 1
                if open_parenthesis_cnt < 0:
                    raise SyntaxError(f"Unmatched closing parenthesis at position {i}.")
            # Add more checks as needed

        if open_parenthesis_cnt != 0:
            raise SyntaxError("Mismatched parentheses in expression.")

    @staticmethod
    def _validate_operators(tokens, factory):
        #  private method of ExpressionEvaluator , used by validate()
        #  method to check the validity of all the operators in the expression
        #  the method iterates over all the iterators and checks them for relevant errors
        #  it uses the execute method of the Operator class to check for relevant errors
        #  if such errors accrue the method throws them to the output along with relevant
        #  reference for the location and syntax in the expression that caused the error
        #  the first token is checked separately in _validate_first_token() and the last
        #  token is checked aside from the others to not risk going out of bounds
        for i in range(1, len(tokens) - 1):
            if tokens[i] in "~+-*/%$&!^@":
                if tokens[i] == '~':
                    try:
                        factory.get_operator('~').execute(tokens[i + 1])
                    except (SyntaxError, TypeError) as e:
                        se_message = e.args[0] if e.args else "Unknown error"
                        raise type(e)(f"at {i + 1}'th-{i + 2}'th characters , "
                                      f"'{tokens[i]}{tokens[i + 1]}' : {se_message} ")
                elif tokens[i] == '!':
                    try:
                        factory.get_operator('!').execute(tokens[i - 1])
                    except (SyntaxError, TypeError) as e:
                        se_message = e.args[0] if e.args else "Unknown error"
                        raise type(e)(f"at {i}'th-{i + 1}'th characters , "
                                      f"'{tokens[i - 1]}{tokens[i]}': {se_message}")
                elif tokens[i] == '-' and (
                        not isinstance(tokens[i - 1], (int, float)) and isinstance(tokens[i + 1], (int, float))):
                    try:
                        factory.get_operator('-').execute(tokens[i + 1])
                    except (SyntaxError, TypeError) as e:
                        se_message = e.args[0] if e.args else "Unknown error"
                        raise type(e)(f"at {i}'th-{i + 1}'th characters , "
                                      f"'{tokens[i - 1]}{tokens[i]}': {se_message}")
                else:
                    try:
                        factory.get_operator(tokens[i]).execute(tokens[i - 1], tokens[i + 1])
                    except (SyntaxError, TypeError) as e:
                        se_message = e.args[0] if e.args else "Unknown error"
                        raise type(e)(f"at {i}'th-{i + 2}'th characters , "
                                      f"'{tokens[i - 1]}{tokens[i]}{tokens[i + 1]}': {se_message}")

        if (tokens[len(tokens) - 1] in "~+-*/%$&^@" or
                (tokens[len(tokens) - 1] == '!' and not isinstance(tokens[len(tokens) - 2], (int, float)))):
            raise SyntaxError("the last element in the expression cant be an operator with no context")

    @staticmethod
    def to_postfix(tokens):
        pass

    @staticmethod
    def evaluate_postfix(postfix_tokens):
        pass
