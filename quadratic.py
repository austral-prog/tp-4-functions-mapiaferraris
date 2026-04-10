# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = (b ** 2 - 4 * a * c)
    if discriminante == 0:
        r12 = (-b + (discriminante ** 0.5)) / (2 * a) 
        return f"({r12})"

    elif discriminante > 0:
        r1 = (-b + (discriminante ** 0.5)) / 2 * a 
        r2 = (-b - (discriminante ** 0.5)) / 2 * a 
        return f"({r1}, {r2})"
    
    else:
        return "( )"
#print(roots ())


def value_y(a, b, c, x):
    y = a * x **2 + b * x + c 
    return (y)
#print(value_y())


def to_string(a, b, c):
    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return f"f(x) = {c}"
#print(to_string())

def derivation(a, b, c):
    der_a = 2 * a
    if der_a != 0 and b != 0:
        return f"f'(x) = {der_a} * X + {b}"
    elif der_a != 0 and b == 0:
        return f"f'(x) = {der_a} * X"
    elif der_a == 0 and b != 0:
        return f"f'(x) = {b}"
    else:
        return f"f'(x) = 0"
#print(derivation())