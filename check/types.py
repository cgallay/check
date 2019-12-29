
class Type:
    def __init__(self):
        self.error_msg = "is not valid"

    def __comply__(self, value, arg_name):
        raise NotImplementedError("This function must be implemented in children class")

    def __check__(self, value, arg_name):
        if not self.__comply__(value, arg_name):
            raise ValueError(
                f"Value {value} for arguemnt {arg_name} {self.error_msg}"
            )


class Choice(Type):
    def __init__(self, allow_values):
        self.allow_values = allow_values
        self.error_msg = "can onlu be part of {self.allow_values}"

    def __comply__(self, value, arg_name):
        return value in self.allow_values
        

class Integer(Type):
    def __init__(self):
        self.error_msg = "must be an Integer"

    def __comply__(self, value, arg_name):
        return isinstance(value, int)


class NoneType(Type):
    def __init__(self):
        self.error_msg = "must be of None value"

    def __comply__(self, value, arg_name):
        return value is None


class Any(Type):
    def __init__(self, types):
        self.types = types
        self.error_msg = f"does not comply with any of the accetpect types in {self.types}" 

    def __comply__(self, value, arg_name):
        return any([_type.__comply__(value, arg_name) for _type in self.types])


# class PositiveInteger(Type, Integer):

