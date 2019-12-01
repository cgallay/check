import functools
import inspect


def arg(_func=None, *, name, value_range=None, choice=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sign = inspect.signature(func)
            d = dict(zip([parm for parm in sign.parameters], args))
            v_to_check = d[name]
            if choice is not None:
                if v_to_check not in choice:
                    raise ValueError(
                        f"Value {v_to_check} for arguemnt {name} not in {choice}"
                    )
            if value_range:
                if v_to_check < value_range[0] or v_to_check > value_range[1]:
                    raise ValueError(
                        f"Value {v_to_check} for argument {name} is out of range {value_range}"
                    )
            value = func(*args, **kwargs)
            return value

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)
