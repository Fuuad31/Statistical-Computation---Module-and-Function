import math

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

def parallelogram_area(base, height):
    """
    This function takes the base and height of a parallelogram and returns the area of the parallelogram.
    """
    if (base < 0 or height < 0):
        raise ValueError("Base and height must be positive")
    else:
        print(f"The area of the parallelogram with base = {base} and height = {height} is {base * height} square units")                 
        return base * height

def tcircle_grad(m, x, y, r):
    """
    This function takes the gradient of a tangent line to a circle, the coordinates of the center of the circle, and the radius of the circle and returns the equation of the tangent line to the circle.
    """
    if (r < 0):
        raise ValueError("Radius must be positive")
    else:
        print(f"The equation of the tangent line to the circle with center = ({x}, {y}) and radius = {r} is y = {m}x + {(y - m * x)} +- sqrt({(r ** 2) * (1 + m ** 2)})")
        return f"y = {m}x + {(y - m * x)} +- sqrt({(r ** 2) * (1 + m ** 2)})"

def tcircle_point(x, y, r, x1, y1):
    """
    This function takes the coordinates of the center of a circle, its radius, and the coordinates of a point and returns the equation of the tangent line to the circle that passes through the point.
    """
    if (r < 0):
        raise ValueError("Radius must be positive")
    elif ((x - x1) ** 2 + (y - y1) ** 2 < r ** 2):
        raise ValueError("The point must be outside the circle")
    elif ((x - x1) ** 2 + (y - y1) ** 2 == r ** 2):
        m = -(x1 - x) / (y1 - y)
        print(f"The equation of the tangent line to the circle with center = ({x}, {y}) and radius = {r} that passes through the tangent point ({x1}, {y1}) is y = {m}x + {y1 - m * x1}")
        return f"y = {m}x + {y1 - m * x1}"
    else:
        m = -(x1 - x) / (y1 - y)
        print(f"The equation of the tangent line to the circle with center = ({x}, {y}) and radius = {r} that passes through the external point ({x1}, {y1}) is y = {m}x + {y - m * x + r**2/(y1-y)}")
        return f"y = {m}x + {y - m * x + r**2/(y1-y)}"

def circle_area(r):
    """
    This function takes the radius of a circle and returns the area of the circle.
    """
    if r<0:
        raise ValueError("Radius must be positive")
    else:
        area = math.pi*r
        return area

def circle_perimeter(r):
    """
    This function takes the radius of a circle and returns the perimeter of the circle.
    """
    if r<0:
        raise ValueError("Radius must be positive")
    else:
        perim=2*math.pi*r
        return perim

def squares_area(a,b = 0):
    """
    This function takes the side of a square and returns the area of the square.
    """
    if (a**2 < 0) or (a*b < 0):
        raise ValueError("Sides must be positive")
    if b == 0:
        return print("Squares area =", [a**2])
    else:
        return print("Squares area =", [a*b])

def trapezoid_area(a,b,t):
    """
    This function takes the two parallel sides and the height of a trapezoid and returns the area of the trapezoid.
    """
    if 0.5*(a+b)*t < 0:
        raise ValueError("Sides must be positive")
    else:
        return print("Trapezoid area =", [0.5*(a+b)*t])
    
def striangle_area(a,b,c):
    """
    a = panjang sisi 1
    b = panjang sisi 2
    c = panjang sisi 3
    """
    if (a + b > c) and (a + c > b) and (b + c > a) and a > 0 and b > 0 and c > 0:
        s = (a+b+c) / 2
        Luas_Segitiga = np.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f"The area of triangle given sides {a}, {b}, {c} is {Luas_Segitiga}.")
        return Luas_Segitiga
    else:
        raise ValueError("The sides do not form a triangle.")

def atriangle_area(a,b,sudut_apit):
    """
    a = panjang sisi 1
    b = panjang sisi 2
    sudut_apit = sudut apit antara a dan b
    """
    if a > 0 and b > 0 and sudut_apit > 0 and sudut_apit < 180:
        sudut_apit_radian = math.radians(sudut_apit)
        Luas_Segitiga = 0.5 * a * b * math.sin(sudut_apit_radian)
        print(f"The area of triangle given sides {a}, {b}, and the angle between them {sudut_apit} is {Luas_Segitiga}.")
        return Luas_Segitiga
    else:
        raise ValueError("The sides and the angle should be positive.")