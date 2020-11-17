def _and(a, b):
    return a and b


def _or(a, b):
    return a or b


def _xor(a, b):
    return a ^ b


def _not(a):
    return not a


def _nand(a, b):
    return not(a and b)


def _xnor(a, b):
    return a == b


def _nor(a, b):
    return not(a or b)
