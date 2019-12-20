import functools
import inspect


def arg(_func=None, *, name, vtype, doc=""):
    def decorator(func):
        metadata = {"name": name, "vtype": vtype, "help": doc}
        if hasattr(func, '_args'):
            func._args.append(metadata)
        else:
            func._args = [metadata]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sign = inspect.signature(func)
            d = dict(zip([parm for parm in sign.parameters], args))
            d.update(kwargs)
            v_to_check = d[name]

            if vtype is not None:
                vtype.__check__(v_to_check, name)
            value = func(*args, **kwargs)
            return value

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)


def print_help(func):
    print("Docs:")
    print("Arguments:")
    for arg in func._args:
        print(f"\t{arg['name']} : {arg['help']}")
    print("Returns:")