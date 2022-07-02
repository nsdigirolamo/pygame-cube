from point import Point
from vector import Vector


class Line:
    """
    Represents an infinite line in 3D space.

    Attributes:
        point: Point
            a Point on the Line
        direction: Vector
            a Vector that represents the direction of the Line from the Point
    """

    def __init__(self, point: Point, direction: Vector):
        """
        Instantiates a new Line.

        :param point: a Point on the Line
        :param direction: a Vector that represents the direction of the Line from the Point
        """
        self.point = point
        self.direction = direction

    def __repr__(self):
        return f"Line({self.point},{self.direction})"

    def has_point(self, point: Point):
        """
        Determines if some given Point exists on the Line.

        The equation of a line with direction vector d = (l, m, n) that passes through the point (x1, y1, z1) is given
        by the formula (x-x1)/l = (y-y1)/m = (z-z1)/n where l, m, and n are non-zero real numbers. If l, m, or n are
        zero, then the corresponding x, y, or z needs to be compared directly to x1, y1, or z1. More info:
        https://brilliant.org/wiki/3d-coordinate-geometry-equation-of-a-line/
        :param point: some Point
        :return: True if the Point exists on the Line, False otherwise
        """

        l = self.direction.x != 0
        m = self.direction.y != 0
        n = self.direction.z != 0

        if l and m and n:
            return (point.x - self.point.x) / self.direction.x == (point.y - self.point.y) / self.direction.y == \
                   (point.z - self.point.z) / self.direction.z

        elif not l and m and n:
            return point.x == self.point.x and \
                   (point.y - self.point.y) / self.direction.y == (point.z - self.point.z) / self.direction.z
        elif not m and l and n:
            return point.y == self.point.y and \
                   (point.x - self.point.x) / self.direction.x == (point.z - self.point.z) / self.direction.z
        elif not n and l and m:
            return point.z == self.point.z and \
                   (point.x - self.point.x) / self.direction.x == (point.y - self.point.y) / self.direction.y

        elif not l and not m:
            return point.x == self.point.x and point.y == self.point.y
        elif not l and not n:
            return point.x == self.point.x and point.z == self.point.z
        elif not m and not n:
            return point.y == self.point.y and point.z == self.point.z

        else:
            return False
