
class Operand(object):
    #  helper class that contains methods to be committed on potential operands for calculations
    @staticmethod
    def is_number(token):
        #  method checks if token represents a number -
        #  (actual numeric value or a number represented by a string)
        try:
            float(token)
            return True
        except ValueError:
            return False

    @staticmethod
    def convert_to_number(value):
        #  method converts value into its numeric value
        #  if value is already a numeric value it will
        #  be returned with no changes , if value is a string
        #  the numeric value it represents will be returned (if a value is properly represented in the string)
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"The string '{value}' is not a valid number.")

    @staticmethod
    def is_white_space(element):
        return element in " \t"
