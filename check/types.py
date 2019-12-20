class Type:
    def __check__(self, value, arg_name):
        raise NotImplementedError("This function must be implemented in children class")


class Choice(Type):
    def __init__(self, allow_values):
        self.allow_values = allow_values

    def __check__(self, value, arg_name):
        if value not in self.allow_values:
            raise ValueError(
                f"Value {value} for arguemnt {arg_name} can only be part of {self.allow_values}"
            )

        return value in self.allow_values


class Integer(Type):
    def __check__(self, value, arg_name):
        if int(value) != value:
            raise ValueError(f"Value {value} for argument {arg_name} is not an integer")
# class PositiveInteger(Type, Integer):

