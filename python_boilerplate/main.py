# noqa: E501

def ADD(a,b):return a +  b  # bad name, spacing, formatting


def divide(a: int, b: int) -> int:
    """
    Divides two numbers.
    """
    return a / b  # type error: returns float, annotation says int


def greet(name, excited=False):
    if excited == True:
        return "Hello " + name + "!!!"
    else:
        return "Hello "+  name


def returns_none(flag: bool) -> int:
    if flag:
        return 42
    # implicit None return


def unused_function(x: int, y: int):
    z = x + y  # unused variable
    pass