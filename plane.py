from line import Line
from point import Point
from vector import Vector, dot_product


class Plane:
    """
    Represents an infinite plane in 3D space.

    Attributes:
        point: Point
            a Point on the Plane
        normal: Vector
            a Vector normal to the Plane
    """

    def __init__(self, point: Point, normal: Vector):
        """
        Instantiates a new Plane.

        :param point: a Point on the Plane
        :param normal: a Vector normal to the Plane
        """
        self.point = point
        self.normal = normal

    def __repr__(self):
        return f"Plane({self.point},{self.normal})"

    def has_point(self, point: Point):
        """
        Determines if some given Point exists on the Plane.

        The equation of a plane through a point A = (x1, y1, z1) whose normal vector is n = (a, b, c) is
        a(x-x1) + b(y-y1) + c(z-z1) = 0. See this link for more information:
        https://brilliant.org/wiki/3d-coordinate-geometry-equation-of-a-plane/
        :param point: some Point
        :return: True if the Point exists on the Plane, False otherwise
        """
        a = self.normal.x
        b = self.normal.y
        c = self.normal.z
        x1 = self.point.x
        y1 = self.point.y
        z1 = self.point.z
        x = point.x
        y = point.y
        z = point.z
        return a * (x - x1) + b * (y - y1) + c * (z - z1) == 0

    def get_intersection(self, line: Line):
        """
        Determines if some given Line intersects the Plane.

        There's a lot of math going on here that I don't really understand; I just know the equation works. Look at this
        wikipedia page because I honestly don't have a great grasp at what's going on:
        https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection
        :param line: some Line
        :return: the Point where the Line intersects with the Plane, None if no such Point exists
        """
        plane_normal = self.normal
        plane_point = self.point
        line_vector = line.direction
        line_point = line.point
        point_difference = plane_point - line_point

        numerator = point_difference.x * plane_normal.x + point_difference.y * plane_normal.y + \
            point_difference.z * plane_normal.z
        denominator = dot_product(line_vector, plane_normal)

        if denominator != 0:
            d = numerator / denominator
            intersect = Point(line_point.x + line_vector.x * d, line_point.y + line_vector.y * d, line_point.z + line_vector.z * d)
            return intersect
        else:
            return None
