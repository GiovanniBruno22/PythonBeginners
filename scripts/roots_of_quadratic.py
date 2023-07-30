def roots(a,b,c):
    """
    Calculate and print the roots of a quadratic equation.
    The quadratic equation is in the form ax^2 + bx + c = 0, where a, b, and c are coefficients.
    Example: roots of x^2 - 3x + 2 = 0 are  2 and  1
            Input: 1,-3,2
            Output: 2.0 and 1.0
    """
    a = float(a)
    b = float(b)
    c = float(c)
    x1 = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    x2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    print("The roots are:", x1, " and ", x2)

if __name__ == "__main__":
    a, b, c = input("Enter the values of a, b, and c (seperated by commas) for the equation ax^2 + bx + c = 0 : ").split(',')
    roots(a,b,c)
