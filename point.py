class Point:
    """
    Represents a point in 3D space.

    Attributes:
        x: float
            the Point's x position
        y: float
            the Point's y position
        z: float
            the Point's z position
    """

    def __init__(self, x: float, y: float, z: float):
        """
        Instantiates a new Point.

        :param x: the Point's x position
        :param y: the Point's y position
        :param z: the Point's z position
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        """
        Determines if the Point is equal to some other given Point.

        Two Points are equal if their x, y, and z components are all equal.
        :param other: another Point
        :return: True if the two Points are equal, False otherwise
        """
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        """
        Adds the x, y, and z positions of the Point and some other given Point.

        :param other: another Point
        :return: the sum of the two Points
        """
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Subtracts the x, y, and z positions of the Point and some other given Point.

        :param other: another Point
        :return: the difference between the two Points
        """
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __round__(self, n):
        """Rounds the x, y, and z components of the Vector by some given amount n."""
        return Point(round(self.x, n), round(self.y, n), round(self.z, n))