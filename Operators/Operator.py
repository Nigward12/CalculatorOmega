from builtins import staticmethod

from SingletonMeta import SingletonMeta


class Operator(object, metaclass=SingletonMeta):
    # basic abstract class for all operator classes ,
    # each instance holds the symbol char , the placement it should be in compared to
    # its operand or operands and its priority
    # execute method will be overriden in subclasses and will include a logic
    # to execute the action of each operator
    def __init__(self, symbol, placement, priority):
        self.symbol = symbol
        self.placement = placement
        self.priority = priority

    def execute(self, operand1, for_validation, operand2=None):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def __str__(self):
        return self.symbol

    #  the methods below are used to return a comparison string
    #  to check if a character is an operator of some kind
    #  used in the subclasses of operator to avoid circular imports
    #  from operator factory (it also contains an operator list
    #  but imports operatorSubClasses)
    # and also to avoid dependency between Operator and its subclasses on other classes
    # which allows use of these classes as a standalone
    @staticmethod
    def operators_str():
        return "+-*/!@#$%&^~"

    @staticmethod
    def right_operators_str():
        return "!#"

    @staticmethod
    def left_operators_str():
        return "~_;"

