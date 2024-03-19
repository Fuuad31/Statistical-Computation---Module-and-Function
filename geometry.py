def inradius(a,b,c):
    """
    This function takes three sides of a triangle and returns the inradius of the triangle.
    """
    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("The sides do not form a triangle.")
    elif a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The sides should be positive.")

    s = (a+b+c)/2
    print(f'Inradius of the triangle: {(s*(s-a)*(s-b)*(s-c))**0.5/s}')
    return ((s*(s-a)*(s-b)*(s-c))**0.5)/s

def outradius(a,b,c):
    """
    This function takes three sides of a triangle and returns the outradius of the triangle.
    """
    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("The sides do not form a triangle.")
    elif a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The sides should be positive.")

    s = (a+b+c)/2
    L = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f'Radius of the circumcircle: {a*b*c/(4*L)}')
    return a*b*c/(4*L)

    