# 6.00 Problem Set 2
#
# Successive Approximation: Newton's Method
#
# Name          : Solutions
# Collaborators : <your collaborators>
# Time spent    : <total time>
#

poly = (0.0,0.0,5.0,9.3,7.0)
x= -13

def evaluate_poly(poly, x):
    
    total = 0.0
    for i in range(len(poly)):
        total += poly[i] * (x ** i)
    return total
evaluate_poly(poly,x)

poly1 = (-13.39,0.0,17.5,3.0,1.0)


def compute_deriv(poly):
    
    poly_deriv = []
    if len(poly) < 2:
        return [0.0]
    for j in range(1, len(poly)):
        poly_deriv.append(float(j * poly[j]))
    return poly_deriv
    
compute_deriv(poly1)
def compute_root(poly, x_0, epsilon):
    """
    
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = [-13.39, 0.0, 17.5, 3.0, 1.0]    # - 13.39 + 17.5x^2 + 3x^3 + x^4
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    [0.80679075379635201, 8]

    poly: list of numbers, length > 1.
         Represents a polynomialfunction containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    """
    root = x_0
    counter = 1
    while abs(evaluate_poly(poly, root)) >= epsilon:
        root = (root - evaluate_poly(poly, root) /
                evaluate_poly(compute_deriv(poly), root))
        counter += 1
    return [root, counter]
