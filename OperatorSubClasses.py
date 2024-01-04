from Operator import Operator
from SingletonMeta import SingletonMeta
import math


class AddOperator(Operator):
    # class handles the building and executing of the addition action between two operands
    def __init__(self):
        super().__init__('+', "middle", 1)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("Addition requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return operand1 + operand2


class SubOperator(Operator):
    # class handles the building and executing of the Subtraction action between two operands
    # or the negation action on an operand
    def __init__(self):
        super().__init__('-', "middle", 1)

    def execute(self, operand1, operand2=None):
        if operand2 is None:
            if operand1 is None:
                raise ValueError("Unary negation requires one operand")
            if not isinstance(operand1, (int, float)):
                raise TypeError("Operand must be numeric")
            return -operand1
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return operand1 - operand2


class MulOperator(Operator):
    # class handles the building and executing of the Multiplication action between two operands
    def __init__(self):
        super().__init__('*', "middle", 2)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("Multiplication requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return operand1 * operand2


class DivOperator(Operator):
    # class handles the building and executing of the Division action between two operands
    def __init__(self):
        super().__init__('/', "middle", 2)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("Division requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return operand1 / operand2


class PowerOperator(Operator):
    # class handles the building and executing of the Exponentiation action between two operands
    def __init__(self):
        super().__init__('^', "middle", 3)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("Exponentiation requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return math.pow(operand1, operand2)


class ModuloOperator(Operator):
    # class handles the building and executing of the Modulo action between two operands
    def __init__(self):
        super().__init__('%', "middle", 4)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("modulo operation requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return operand1 % operand2


class AvgOperator(Operator):
    # class handles the building and executing of the Average action between two operands
    def __init__(self):
        super().__init__('@', "middle", 5)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("Average operation requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return (operand1 + operand2) / 2


class MaxOperator(Operator):
    # class handles the building and executing of the Maximum action between two operands
    def __init__(self):
        super().__init__('$', "middle", 5)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("Max operation requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return operand1 if operand1 > operand2 else operand2


class MinOperator(Operator):
    # class handles the building and executing of the Exponentiation Minimum between two operands
    def __init__(self):
        super().__init__('&', "middle", 5)

    def execute(self, operand1, operand2=None):
        if operand2 is None or operand1 is None:
            raise ValueError("Min operation requires two operands")
        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            raise TypeError("Operands must be numeric")
        return operand1 if operand1 < operand2 else operand2


class FactorialOperator(Operator):
    # class handles the building and executing of the Factorial action on an operand
    def __init__(self):
        super().__init__('!', "right", 6)

    def execute(self, operand1, operand2=None):
        if operand1 is None:
            raise ValueError("Factorial operation requires an operator")
        if not isinstance(operand1, (int, float)):
            raise TypeError("Operand must be numeric")
        result = 1
        for i in range(2, operand1 + 1):
            result *= i
        return result


class TildaOperator(Operator):
    # class handles the building and executing of the Tilda action on an operand
    def __init__(self):
        super().__init__('~', "left", 6)

    def execute(self, operand1, operand2=None):
        if operand1 is None:
            raise ValueError("TildaOperation requires an operator")
        if not isinstance(operand1, (int, float)):
            raise TypeError("Operand must be numeric")
        return -operand1
