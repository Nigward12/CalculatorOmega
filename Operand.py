class Operand(object):
    # this class saves the value of an operand
    # in an object , this adds for the Clarity and Readability
    # of the code and provides freedom for adding functionality to operands
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)