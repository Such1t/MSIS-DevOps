def divide(a: int,b: int) ->float:
    if b == 0:
        raise ValueError("Cannot divde by zero")
    return a / b

def multiply(a: int,b: int) ->int:
    return a*b
