import math


def dotprod2v(a, b, theta):
    """

    :param a: Magnitude of first vector in Newtons
    :param b: Magnitude of second vector in Newtons
    :param theta: Angle between degrees
    """
    return a * b * math.cos(math.radians(theta))  # Dot product function


A = int(input("Enter the magnitude of first vector in Newtons: "))
B = int(input("Enter the magnitude of second vector in Newtons: "))
Theta = int(input("Enter the angle between vectors in degrees: "))

d2p = dotprod2v(A, B, Theta)

print("The dot-product is", d2p)  # Print dot product
