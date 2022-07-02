from math import sqrt, acos


class Vector:
    """
    Represents a vector in 3D space.

    Attributes:
        x: float
            the Vector's x component
        y: float
            the Vector's y component
        z: float
            the Vector's z component
    """

    def __init__(self, x: float, y: float, z: float):
        """
        Instantiates a new Vector.

        :param x: the Vector's x component
        :param y: the Vector's y component
        :param z: the Vector's z component
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"

    def __add__(self, other):
        """
        Adds the x, y, and z components of the Vector and some other given Vector.

        :param other: another Vector
        :return: the sum of the two Vectors
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Subtracts the x, y, and z components of the Vector and some other given Vector.
        
        :param other: another Vector
        :return: the difference between the two Vectors
        """""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __round__(self, n):
        """Rounds the x, y, and z components of the Vector by some given amount n."""
        return Vector(round(self.x, n), round(self.y, n), round(self.z, n))

    def __eq__(self, other):
        """Checks equality between two Vectors."""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def get_magnitude(self):
        """Calculates and returns the magnitude of the Vector."""
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def get_unit_vector(self):
        """Calculates and returns the direction of the Vector."""
        magnitude = self.get_magnitude()
        if magnitude != 0:
            return Vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)
        else:
            return Vector(0, 0, 0)


def cross_product(vector1: Vector, vector2: Vector):
    """
    Calculates and returns the cross product of two given Vectors.
    """
    x = vector1.y * vector2.z - vector1.z * vector2.y
    y = vector1.z * vector2.x - vector1.x * vector2.z
    z = vector1.x * vector2.y - vector1.y * vector2.x
    return Vector(x, y, z)


def dot_product(vector1: Vector, vector2: Vector):
    """Calculates and returns the dot product of two given Vectors"""
    return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z


def get_angle(vector1: Vector, vector2: Vector):
    """Calculates and returns the angle between two given vectors"""
    return acos(dot_product(vector1, vector2) / (vector1.get_magnitude() * vector2.get_magnitude()))

