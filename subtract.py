def subtract(a, b, *args):
    result = a - b
    for x in args:
        result -= x
    return result
