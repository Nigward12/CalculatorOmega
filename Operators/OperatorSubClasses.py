from Operators.Operator import Operator
import math
from Operand import Operand


#  this file contains all the operators that are subclasses of operator upper class
#  each operator has his own logic for validation and output
#  each operator realized the abstract method execute from operator
#  this method has two options for execution , one is used only for input validation
#  and checks if the operands received are placed logically correct for the operators context
#  for this execution option the for_validation input variable of the method must be true
#  the second option of execution for the execute method is for the actual calculation
#  of the action the class represents on the operands that were sent , in this option
#  for_validation must be false and the operands must be a numeric value

#  a small part of the errors that can rise up in the execute method of the operators
#  will most likely never rise up in this specific project but are there to allow
#  use of these classes on their own outside of this specific project (theoretically)
class AddOperator(Operator):
    # Handles the addition action between two operands
    def __init__(self):
        super().__init__('+', "middle", 1)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Addition requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("+ placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        return operand1 + operand2


class SubOperator(Operator):
    # Handles the subtraction action between two operands or negation
    def __init__(self):
        super().__init__('-', "middle", 1)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Subtraction requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("- placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        return operand1 - operand2


class MulOperator(Operator):
    # Handles the multiplication action between two operands
    def __init__(self):
        super().__init__('*', "middle", 2)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Multiplication requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("* placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        return operand1 * operand2


class DivOperator(Operator):
    # Handles the division action between two operands
    def __init__(self):
        super().__init__('/', "middle", 2)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Division requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("/ placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        try:
            return operand1 / operand2
        except ZeroDivisionError:
            raise ZeroDivisionError("cant divide by zero")


class PowerOperator(Operator):
    # Handles the exponentiation action between two operands
    def __init__(self):
        super().__init__('^', "middle", 3)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Exponentiation requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("^ placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        try:
            return math.pow(operand1, operand2)
        except ValueError:
            if operand1 == 0:
                raise ZeroDivisionError("cant raise zero by a negative number - division by zero")
            else:
                raise ValueError("cant raise a negative number by a non integer number - complex result")


class ModuloOperator(Operator):
    # Handles the modulo action between two operands
    def __init__(self):
        super().__init__('%', "middle", 4)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Modulo operation requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("% placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        return operand1 % operand2


class AvgOperator(Operator):
    # Handles the average action between two operands
    def __init__(self):
        super().__init__('@', "middle", 5)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Average operation requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("@ placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        return (operand1 + operand2) / 2


class MaxOperator(Operator):
    # Handles the maximum action between two operands
    def __init__(self):
        super().__init__('$', "middle", 5)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Max operation requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("$ placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        return max(operand1, operand2)


class MinOperator(Operator):
    # Handles the minimum action between two operands
    def __init__(self):
        super().__init__('&', "middle", 5)

    def execute(self, operand1, for_validation, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Min operation requires two operands")
        if for_validation:
            #  in the expression , a 'middle' operator can be placed next to parenthesis from both sides
            #  , a number , after a 'right' operator and before a 'left' operator
            if not ((Operand.is_number(operand1) or operand1 == ')' or operand1 in Operator.right_operators_str())
                    and (Operand.is_number(
                        operand2) or operand2 == '(' or operand2 in Operator.left_operators_str())):
                raise SyntaxError("& placed out of context")
            return
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        return min(operand1, operand2)


class FactorialOperator(Operator):
    # Handles the factorial action on an operand
    def __init__(self):
        super().__init__('!', "right", 6)

    def execute(self, operand1, for_validation, operand2=None):
        if operand1 is None:
            raise SyntaxError("Factorial operation requires an operand")
        if for_validation:
            #  in the expression , a 'right' operator can be placed after a closing parenthesis
            #  , a number or another 'right' operator , right operators are always stackable
            if not (Operand.is_number(operand1) or operand1 == ')'
                    or operand1 in Operator.right_operators_str()):
                raise SyntaxError("! placed out of context")
            return
        if not Operand.is_number(operand1) or operand1 < 0 or int(operand1) != operand1:
            raise TypeError("Operand for factorial operation must be a natural number")
        result = 1
        #  factorial operation on the number
        for i in range(2, int(operand1) + 1):
            result *= i
        return result


class SumDigitsOperator(Operator):
    # Handles the sum of digits action on an operand
    def __init__(self):
        super().__init__('#', "right", 6)

    def execute(self, operand1, for_validation, operand2=None):
        if operand1 is None:
            raise SyntaxError("Sum digits requires an operand")
        if for_validation:
            #  in the expression , a 'right' operator can be placed after a closing parenthesis
            #  , a number or another 'right' operator, right operators are always stackable
            if not (Operand.is_number(operand1) or operand1 == ')'
                    or operand1 in Operator.right_operators_str()):
                raise SyntaxError("# placed out of context")
            return
        if not Operand.is_number(operand1) or Operand.convert_to_number(operand1) < 0:
            raise TypeError("Operand for SumDigits must be numeric and positive")
        operand_str = str(operand1)
        # for very .... very .... long numbers
        if 'e' in operand_str or 'E' in operand_str:
            operand_str = '{:.0f}'.format(operand1)  # not accurate a lot of the times
            print(f" *Warning* : operand for digit summing :{operand1} , is represented by a scientific notation \n"
                  f"result may not be accurate")
        # remove decimal point
        operand_str = operand_str.replace('.', '')
        # sum the digits and return them
        return sum(int(digit) for digit in operand_str if digit.isdigit())


class TildaOperator(Operator):
    # Handles the negation action on an operand
    # also used for high priority unary negation ( 4+-(4) -> 4+~(4) )
    def __init__(self):
        super().__init__('~', "left", 6)

    def execute(self, operand1, for_validation, operand2=None):
        if operand1 is None:
            raise SyntaxError("Tilda Operation requires an operand")
        if for_validation:
            #  in the expression , a 'left' operator can be placed before an opening parenthesis
            #  or a number or a left operator different from himself (with a different affect)
            if not (Operand.is_number(operand1) or operand1 == '('
                    or (operand1 in Operator.left_operators_str() and operand1 != self.symbol)):
                raise SyntaxError("~ placed out of context")
            return
        if not Operand.is_number(operand1):
            raise TypeError("Operand must be numeric")
        return -operand1


class LowPriorityUnaryNegation(Operator):
    #  handles the unary negation of an operand
    #  in cases where it overpowered in terms of priority by other operations
    #  (-3! -> _3! -> -6 , '!' overpowers '_' )
    #  only used as a marker after the tokenization has confirmed a valid unary negation attempt
    #  in this project an error shouldn't be raised from this class's execute method
    #  because unary negation is validated in the tokenization process
    #  errors were added for a case of separate use of this class as a standalone
    def __init__(self):
        super().__init__('_', "left", 2.5)

    def execute(self, operand1, for_validation, operand2=None):
        if operand1 is None:
            raise SyntaxError("unary negation Operation requires an operand")
        if for_validation:
            #  in the expression , a 'left' operator can be placed before an opening parenthesis
            #  or a number or a left operator different from himself (with a different affect)
            if not (Operand.is_number(operand1) or operand1 == '('
                    or (operand1 in Operator.left_operators_str() and operand1 != self.symbol)):
                raise SyntaxError("_ placed out of context")
            return
        if not Operand.is_number(operand1):
            raise TypeError("Operand must be numeric")
        return -operand1


class HighPriorityUnaryNegation(Operator):
    #  handles the unary negation of an operand
    # used for high priority unary negation , cases like: ( 4+-(4) -> 4+;(4) -> 4-4 -> 0 )
    #  only used as a marker after the tokenization has confirmed a valid unary negation attempt
    #  in this project an error shouldn't be raised from this class's execute method
    #  because unary negation is validated in the tokenization process
    #  errors were added for a case of separate use of this class as a standalone
    def __init__(self):
        super().__init__(';', "left", 7)

    def execute(self, operand1, for_validation, operand2=None):
        if operand1 is None:
            raise SyntaxError("unary negation Operation requires an operand")
        if for_validation:
            #  in the expression , a 'left' operator can be placed before an opening parenthesis
            #  or a number or a left operator different from himself (with a different affect)
            if not (Operand.is_number(operand1) or operand1 == '('
                    or (operand1 in Operator.left_operators_str() and operand1 != self.symbol)):
                raise SyntaxError("; placed out of context")
            return
        if not Operand.is_number(operand1):
            raise TypeError("Operand must be numeric")
        return -operand1
