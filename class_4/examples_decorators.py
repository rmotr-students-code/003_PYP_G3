__all__ = []

__init__.py


def only_int_arguments(f):

    def wrapped(x, y):
        if type(x) != int or type(y) != int:
            raise ValueError("Just INT args please")
        return f(x, y)

    return wrapped


# @only_int_arguments
def add(x, y):
    return x + y

# [add](2,3)
#  20   21

x = only_int_arguments(add)
print x(2, "a")
