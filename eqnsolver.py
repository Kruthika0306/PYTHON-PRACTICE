import re

def solve_equation(equation):
    # Remove spaces
    equation = equation.replace(" ", "")

    # Split LHS and RHS
    lhs, rhs = equation.split("=")

    # Extract coefficient of x
    x_coeff = re.findall(r'([+-]?\d*)x', lhs)
    if x_coeff[0] in ['', '+']:
        a = 1
    elif x_coeff[0] == '-':
        a = -1
    else:
        a = int(x_coeff[0])

    # Extract constant
    constant = re.sub(r'[+-]?\d*x', '', lhs)
    b = int(constant) if constant else 0

    # RHS value
    c = int(rhs)

    # Solve: ax + b = c → x = (c - b)/a
    x = (c - b) / a

    return x


# Main program
eq = input("Enter equation (e.g., 2x + 3 = 7): ")
result = solve_equation(eq)

print(f"Solution: x = {result}")
