import sys

from basic_operations import addition, substraction


def operation(*args):
    """This is the main routine.

    Parameters
    ----------
    a : built-in types

    b : built-in types

    """
    x, y = float(args[0]), float(args[1])
    a = addition(x, y)
    print('{} + {} is {}'.format(x, y, a))

    b = substraction(x, y)
    print('{} - {} is {}'.format(x, y, b))


if __name__ == '__main__':
    operation(sys.argv[1], sys.argv[2])

# operation(sys.argv[1], sys.argv[2])

    