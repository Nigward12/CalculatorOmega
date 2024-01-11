
class Operand(object):

    @staticmethod
    def is_number(token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    @staticmethod
    def convert_to_number(value):
        if Operand.is_number(value):
            return value
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"The string '{value}' is not a valid number.")

