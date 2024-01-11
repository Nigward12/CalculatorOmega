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

    def execute(self, operand1, operand2=None):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def __str__(self):
        return self.symbol

