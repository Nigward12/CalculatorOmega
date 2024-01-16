from Operand import Operand
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
        factory = OperatorFactory()
        element = ""
        previous_char = None
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isdigit() or char == ".":  # handling the conjoining of adjacent digits
                element += char  # or decimal point to one token
            elif char in " \t":  # just for readability and understanding whitespaces between digits (5  5->55)
                pass
            else:
                if element:
                    element = ExpressionEvaluator._before_appending(tokens, element)
                    if element.strip():
                        # a case where an element was only made of unary signs like
                        # 4+-(4) ,_before_appending() method will already append
                        # the unary negation char to the list and there won't be
                        # any number left to append , the value for the negation
                        # will come from the parenthesis in calculation
                        tokens.append(element)
                    element = ""
                if (char == '-' and (previous_char is None
                                     or (factory.operators.__contains__(previous_char) and
                                         factory.get_operator(
                                             previous_char).placement != "right") or previous_char == '(')):
                    #  add all the consecutive unary negation signs into one token
                    while i < len(expression) and expression[i] == '-':
                        element += "-"
                        i += 1
                    if i == len(expression) or factory.operators.__contains__(expression[i]):
                        # unary signing can only work on a number or parenthesis
                        raise SyntaxError("unary negative signing has no context")
                    previous_char = expression[i - 1]
                    continue
                elif char in "()" or char in factory.operators:
                    tokens.append(char)
                elif char in " \t":
                    pass
                else:
                    raise SyntaxError(f"Invalid character '{char}' in input expression")
            previous_char = char
            i += 1
        if element:  # adding the last number in a case where
            element = ExpressionEvaluator._before_appending(tokens, element)
            if element.strip():
                tokens.append(element)  # the last token in the expression is a number
        return tokens

    @staticmethod
    def _before_appending(tokens, element):
        #  private method of ExpressionEvaluator , used by tokenize() method
        #  method checks and fixes an operand element before appending it to the tokens list
        factory = OperatorFactory()
        if '-' in element:  # handling the tokenization adjacent negative signing of a number
            count = element.count('-')  # (like ------3=3 , ---3=-3)
            element = element[count:]
            if count % 2 != 0:  # unary negation doesn't count if there is an even number of '-'
                if len(tokens) == 0 or tokens[len(tokens) - 1] == "(":
                    tokens.append('_')  # unary negation has low priority
                else:
                    tokens.append(';')  # unary negation has high priority
        if '.' in element:  # validating decimal point placement
            # element can only have one decimal point and it cant be in the first or end
            # decimal point cannot be placed on its own
            if (not any(char.isdigit() for char in element) or element.startswith('.')
                    or element.endswith('.')):
                raise SyntaxError(" a decimal point is placed without context")
            count = element.count('.')
            if count > 1:  # checking if a number has more than one decimal point within it
                raise SyntaxError("a number can only have one decimal point")
        return element

    @staticmethod
    def validate(tokens):
        #  public method of ExpressionEvaluator
        #  method is used to validate the placement of tokens of a given expression
        #  for correct calculation
        if not tokens:
            raise SyntaxError("The expression is empty.")
        try:
            ExpressionEvaluator._validate_first_token(tokens)
            ExpressionEvaluator._validate_parenthesis(tokens)
            ExpressionEvaluator._validate_operators(tokens)
            ExpressionEvaluator._validate_last_token(tokens)
        except (SyntaxError, TypeError, ZeroDivisionError) as e:
            raise type(e)(f"{e}")

    @staticmethod
    def _validate_first_token(tokens):
        # Private method of ExpressionEvaluator, used by the validate()
        # method to check the validity of the first token in the expression.
        # The first token can't be an operator unless it's a negative sign or tilda with a number after.

        factory = OperatorFactory()
        is_left_placement_operator = (factory.operators.__contains__(tokens[0]) and
                                      factory.get_operator(tokens[0]).placement == "left")
        is_valid_following_token = len(tokens) > 1 and (Operand.is_number(tokens[1]) or
                                                        tokens[1] == '(' or
                                                        (factory.operators.__contains__(tokens[1]) and
                                                         factory.get_operator(tokens[1]).placement == "left" and
                                                         tokens[1] != tokens[0]))

        is_bad_operator = tokens[0] in factory.operators and not is_left_placement_operator

        # Check if the first token is an invalid operator
        if is_bad_operator or (is_left_placement_operator and not is_valid_following_token) or tokens[0] == ")":
            raise SyntaxError(f"first character in expression is placed out of context")

    @staticmethod
    def _validate_parenthesis(tokens):
        #  private method of ExpressionEvaluator , used by validate()
        #  method to check the validity of all the parenthesis in the expression
        #  checks that each opening parenthesis has closing ones and that there are no
        #  more parenthesis of one kind than the other , also checks for empty parenthesis
        open_parenthesis_cnt = 0
        for i in range(0, len(tokens)):
            if Operand.is_number(tokens[i]) and i < len(tokens) - 1 and tokens[i + 1] == "(":
                raise SyntaxError("No suggested multiplication on parenthesis in this calculator")
            if tokens[i] == '(':
                # open parenthesis in the end of the expression
                # a separate if is needed to avoid going out of bounds in the tokens list
                if i == len(tokens) - 1:
                    raise SyntaxError("open parenthesis in the end of the expression")
                if (tokens[i + 1]) == ')':
                    raise SyntaxError(f"at {i + 1}'th-{i + 2}'th characters, '()', empty parenthesis are not allowed")
                open_parenthesis_cnt += 1
            elif tokens[i] == ')':
                open_parenthesis_cnt -= 1
                if open_parenthesis_cnt < 0:
                    raise SyntaxError("Mismatched parentheses in expression.")
            # Add more checks as needed

        if open_parenthesis_cnt != 0:
            raise SyntaxError("Mismatched parentheses in expression.")

    @staticmethod
    def _validate_operators(tokens):
        #  private method of ExpressionEvaluator , used by validate()
        #  method is used to check the validity of all the operators in the expression
        #  the method iterates over all the iterators and checks them for relevant errors
        #  it uses the execute method of the Operator class to check for relevant errors
        #  if such errors accrue the method throws them to the output along with relevant
        #  reference for the location and syntax in the expression that caused the error
        #  the first token is checked separately in _validate_first_token() and the last
        #  token is checked aside from the others to not risk going out of bounds
        factory = OperatorFactory()
        for i in range(1, len(tokens) - 1):
            if factory.operators.__contains__(tokens[i]):
                if factory.get_operator(tokens[i]).placement == "left":
                    #  left operator works on the next token in the expression
                    try:
                        factory.get_operator('~').execute(tokens[i + 1], True)
                    except (SyntaxError, TypeError) as e:
                        se_message = e.args[0] if e.args else "Unknown error"
                        raise type(e)(f"at {i + 1}'th-{i + 2}'th tokens , "
                                      f"'{tokens[i]}{tokens[i + 1]}' : {se_message} ")
                elif factory.get_operator(tokens[i]).placement == "right":
                    #  right operator works on the previous token in the expression
                    try:
                        factory.get_operator(tokens[i]).execute(tokens[i - 1], True)
                    except (SyntaxError, TypeError) as e:
                        se_message = e.args[0] if e.args else "Unknown error"
                        raise type(e)(f"at {i}'th-{i + 1}'th tokens , "
                                      f"'{tokens[i - 1]}{tokens[i]}': {se_message}")
                else:
                    #  middle operator works on the previous and next tokens
                    try:
                        factory.get_operator(tokens[i]).execute(tokens[i - 1], True, tokens[i + 1])
                    except (SyntaxError, TypeError, ZeroDivisionError) as e:
                        se_message = e.args[0] if e.args else "Unknown error"
                        raise type(e)(f"at {i}'th-{i + 2}'th tokens , "
                                      f"'{tokens[i - 1]}{tokens[i]}{tokens[i + 1]}': {se_message}")

    @staticmethod
    def _validate_last_token(tokens):
        #  private method of ExpressionEvaluator , used by validate()
        #  method is used to check the validity of the last token in the expression
        #  last token can only be operator with its placement property being "right" (of  a number
        #  or another right sided operator)
        #  , a closing parenthesis and a number that is placed after a middle or left sided operator
        factory = OperatorFactory()
        last_token = tokens[len(tokens) - 1]
        second_last_token = tokens[len(tokens) - 2]
        last_is_operator = factory.operators.__contains__(last_token)
        second_last_is_operator = factory.operators.__contains__(second_last_token)
        error_found = False
        if last_is_operator:
            last_operator = factory.get_operator(last_token)
            if not last_operator.placement == "right":
                error_found = True
            elif second_last_is_operator:
                second_last_operator = factory.get_operator(second_last_token)
                if not second_last_operator.placement == "right":
                    error_found = True
            elif not (Operand.is_number(second_last_token) or second_last_token == ')'):
                error_found = True
        if Operand.is_number(last_token):
            if second_last_is_operator:
                second_last_operator = factory.get_operator(second_last_token)
                if second_last_operator.placement == "right":
                    error_found = True
            if second_last_token == ')':
                error_found = True
        if error_found:
            raise SyntaxError("the last element in the expression is placed out of context")

    @staticmethod
    def to_postfix(tokens):
        postfix_tokens = []  # output list that will contain the tokens list after conversion to postfix
        operators = []
        factory = OperatorFactory()

        for i in range(len(tokens)):
            c = tokens[i]

            # If the scanned token is an operand, add it to the output list.
            if Operand.is_number(c):
                postfix_tokens.append(c)
            # If the scanned token is an opening parenthesis, push it to the operator stack.
            elif c == '(':
                operators.append(c)
            # If the scanned token is a closing parenthesis, pop and add to the output list from the operator stack
            # until an opening parenthesis is encountered.
            elif c == ')':
                while operators and operators[-1] != '(':
                    postfix_tokens.append(operators.pop())
                operators.pop()  # Pop the opening parenthesis
            # If the scanned token is an operator
            # , append all operators with lower or equal priority to the output list
            # push the operator to the stack
            # * if the operator is a right sided operator and the top operator in the stack is
            # of equal priority to that of the current operator , no need to pop the stack
            # as the order of the operations will stay correct
            else:
                while operators and (
                        ExpressionEvaluator._precedence(tokens[i]) <= ExpressionEvaluator._precedence(operators[-1])):
                    postfix_tokens.append(operators.pop())
                operators.append(c)

        # Pop all the remaining elements from the stack
        while operators:
            postfix_tokens.append(operators.pop())
        return postfix_tokens  # return the converted list

    @staticmethod
    def _precedence(op):
        #  private method of ExpressionEvaluator , used by to_postfix()
        #  to determine the priority of any given operator while
        #  converting the expression to postfix notation
        factory = OperatorFactory()
        if op in factory.operators:
            return factory.get_operator(op).priority
        else:
            return -1  # will usually happen for an opening parenthesis

    @staticmethod
    def evaluate_postfix(postfix_tokens):
        operand_stack = []
        factory = OperatorFactory()
        # Iterate over the postfix tokens list
        for token in postfix_tokens:

            # If the scanned character is an operand
            #  push it to the operand stack
            if Operand.is_number(token):
                operand_stack.append(Operand.convert_to_number(token))

            # If the scanned character is an operator,
            # pop one operand from the operand stack for unary operators and execute the operation
            # pop two operands from the operand stack for binary operators and execute the operation
            # push the result to the operand stack
            # additional checks for edge cases where unary negation is overpowered in terms of priority
            # - the operation with the higher priority will be executed on the non-negative operand
            # only then the unary negation will be executed on the result
            else:
                current_operator = factory.get_operator(token)
                if current_operator.placement != "middle":
                    val = operand_stack.pop()
                    operand_stack.append(current_operator.execute(val, False))
                else:
                    val1 = operand_stack.pop()
                    val2 = operand_stack.pop()
                    operand_stack.append(current_operator.execute(val2, False, val1))
        return operand_stack.pop()
