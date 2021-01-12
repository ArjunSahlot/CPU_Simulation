def _and(a, b):
    return a.status and b.status


def _or(a, b):
    return a.status or b.status


def _xor(a, b):
    return a.status ^ b.status


def _not(a):
    return not a.status


def _nand(a, b):
    return not(a.status and b.status)


def _xnor(a, b):
    return a.status == b.status


def _nor(a, b):
    return not(a.status or b.status)
