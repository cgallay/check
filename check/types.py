class Type:
    def __init__(self):
        self.error_msg = "is not valid"

    def __comply__(self, value, arg_name):
        raise NotImplementedError("This function must be implemented in children class")

    def __check__(self, value, arg_name):
        if not self.__comply__(value, arg_name):
            raise ValueError(f"Value {value} for arguemnt {arg_name} {self.error_msg}")


class Choice(Type):
    def __init__(self, allow_values):
        self.allow_values = allow_values
        self.error_msg = f"can only be part of {self.allow_values}"

    def __comply__(self, value, arg_name):
        return value in self.allow_values

    def __repr__(self):
        return f"Choice[{', '.join(self.allow_values)}]"


class Integer(Type):
    def __init__(self):
        self.error_msg = "must be an Integer"

    def __comply__(self, value, arg_name):
        return isinstance(value, int)

    def __repr__(self):
        return "Int"


class Float(Type):
    def __init__(self):
        self.error_msg = "must be a Float"

    def __comply__(self, value, arg_name):
        return isinstance(value, float)

    def __repr__(self):
        return "Float"


class String(Type):
    def __init__(self):
        self.error_msg = "must be a string"

    def __comply__(self, value, arg_name):
        return isinstance(value, str)

    def __repr__(self):
        return "Str"


class NoneType(Type):
    def __init__(self):
        self.error_msg = "must be of None value"

    def __comply__(self, value, arg_name):
        return value is None

    def __repr__(self):
        return "None"


class Any(Type):
    def __init__(self, types):
        self.types = types
        self.error_msg = (
            f"does not comply with any of the accetpect types in {self.types}"
        )

    def __comply__(self, value, arg_name):
        return any([_type.__comply__(value, arg_name) for _type in self.types])

    def __repr__(self):
        return f"Any{str(self.types)}"


class RangeFloat(Type):
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.error_msg = f"must be a float contained between {self.lower_bound} and {self.upper_bound}"

    def __comply__(self, value, arg_name):
        return value >= self.lower_bound and value <= self.upper_bound

    def __repr__(self):
        return f"Float[{self.lower_bound}, {self.upper_bound}]"


# class Probability(Type):

