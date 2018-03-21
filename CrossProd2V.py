import math


def crossprod2v(a, b, theta):
    """

    :param a: Magnitude of first vector in Newtons
    :param b: Magnitude of second vector in Newtons
    :param theta: Angle between degrees
    """
    return a * b * math.sin(math.radians(theta))  # cross product function


A = int(input("Enter the magnitude of first vector in Newtons: "))
B = int(input("Enter the magnitude of second vector in Newtons: "))
Theta = int(input("Enter the angle between vectors in degrees: "))

c2p = crossprod2v(A, B, Theta)

print("The cross-product is", c2p)  # Print cross product
