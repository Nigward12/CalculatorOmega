from OperatorSubClasses import (AddOperator, SubOperator, MulOperator, DivOperator, PowerOperator, ModuloOperator,
                                AvgOperator, MaxOperator, MinOperator, FactorialOperator, TildaOperator,
                                SumDigitsOperator, LowPriorityUnaryNegation , HighPriorityUnaryNegation)
from SingletonMeta import SingletonMeta


class OperatorFactory(object, metaclass=SingletonMeta):
    # this factory class is responsible for creating and providing
    # the instances of the operator classes , it holds a dictionary
    # in which each key is an operator sign and each corresponding value is the class itself
    def __init__(self):
        self.operators = {
            '+': AddOperator,
            '-': SubOperator,
            '*': MulOperator,
            '/': DivOperator,
            '^': PowerOperator,
            '%': ModuloOperator,
            '@': AvgOperator,
            '$': MaxOperator,
            '&': MinOperator,
            '!': FactorialOperator,
            '~': TildaOperator,
            '#': SumDigitsOperator,
            '_': LowPriorityUnaryNegation,
            ';': HighPriorityUnaryNegation
        }

    def get_operator(self, symbol):
        # method will  get the class corresponding to the symbol (if its correct) and return its instance
        # (instance will be created if an instance doesn't already exist or be returned if it does according
        # to the logic in singletonMeta class)
        operator_class = self.operators.get(symbol)
        if not operator_class:
            raise ValueError(f"Operator '{symbol}' is not supported.")
        return operator_class()
