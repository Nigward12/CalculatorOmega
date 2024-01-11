from Operator import Operator
from SingletonMeta import SingletonMeta
import math
from Operand import Operand


class AddOperator(Operator):
    # Handles the addition action between two operands
    def __init__(self):
        super().__init__('+', "middle", 1)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Addition requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return operand1 + operand2


class SubOperator(Operator):
    # Handles the subtraction action between two operands or negation
    def __init__(self):
        super().__init__('-', "middle", 1)

    def execute(self, operand1, operand2=None):
        if operand2 is None:
            if operand1 is None:
                raise SyntaxError("Unary negation requires one operand")
            if not Operand.is_number(operand1):
                raise TypeError("Operand must be numeric")
            operand1 = Operand.convert_to_number(operand1)
            return -operand1
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return operand1 - operand2


class MulOperator(Operator):
    # Handles the multiplication action between two operands
    def __init__(self):
        super().__init__('*', "middle", 2)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Multiplication requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return operand1 * operand2


class DivOperator(Operator):
    # Handles the division action between two operands
    def __init__(self):
        super().__init__('/', "middle", 2)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Division requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return operand1 / operand2


class PowerOperator(Operator):
    # Handles the exponentiation action between two operands
    def __init__(self):
        super().__init__('^', "middle", 3)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Exponentiation requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return math.pow(operand1, operand2)


class ModuloOperator(Operator):
    # Handles the modulo action between two operands
    def __init__(self):
        super().__init__('%', "middle", 4)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Modulo operation requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return operand1 % operand2


class AvgOperator(Operator):
    # Handles the average action between two operands
    def __init__(self):
        super().__init__('@', "middle", 5)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Average operation requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return (operand1 + operand2) / 2


class MaxOperator(Operator):
    # Handles the maximum action between two operands
    def __init__(self):
        super().__init__('$', "middle", 5)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Max operation requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return max(operand1, operand2)


class MinOperator(Operator):
    # Handles the minimum action between two operands
    def __init__(self):
        super().__init__('&', "middle", 5)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise SyntaxError("Min operation requires two operands")
        if not Operand.is_number(operand1) or not Operand.is_number(operand2):
            raise TypeError("Operands must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        operand2 = Operand.convert_to_number(operand2)
        return min(operand1, operand2)


class FactorialOperator(Operator):
    # Handles the factorial action on an operand
    def __init__(self):
        super().__init__('!', "right", 6)

    def execute(self, operand1, operand2=None):
        if operand1 is None:
            raise SyntaxError("Factorial operation requires an operand")
        if not Operand.is_number(operand1) or operand1 < 0:
            raise TypeError("Operand must be a natural number")
        operand1 = Operand.convert_to_number(operand1)
        result = 1
        for i in range(2, operand1 + 1):
            result *= i
        return result


class SumDigitsOperator(Operator):
    # Handles the sum of digits action on an operand
    def __init__(self):
        super().__init__('#', "right", 6)

    def execute(self, operand1, operand2=None):
        if operand1 is None:
            raise SyntaxError("Sum digits requires an operand")
        if not Operand.is_number(operand1):
            raise TypeError("Operand must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        return sum(int(digit) for digit in str(operand1))


class TildaOperator(Operator):
    # Handles the negation action on an operand
    def __init__(self):
        super().__init__('~', "left", 6)

    def execute(self, operand1, operand2=None):
        if operand1 is None:
            raise SyntaxError("TildaOperation requires an operand")
        if not Operand.is_number(operand1):
            raise TypeError("Operand must be numeric")
        operand1 = Operand.convert_to_number(operand1)
        return -operand1
