from line import Line
from point import Point
from vector import Vector


class Edge(Line):
    """
    Represents a finite line in 3D space.

    Edge inherits from Line, and is mostly the same. The key difference between an Edge and a Line is that an Edge
    is finite. Lines go on forever, but an Edge is limited between its two given points.

    Attributes:
        point0: Point
            a point at an end of the Edge
        point1: Point
            a point at an end of the Edge
    """

    def __init__(self, point0: Point, point1: Point):
        """
        Instantiates a new Edge.

        :param point0: a point at an end of the Edge
        :param point1: a point at an end of the Edge
        """
        self.point0 = point0
        self.point1 = point1
        super().__init__(point0, Vector(point1.x - point0.x, point1.y - point0.y, point1.z - point0.z))

    def __repr__(self):
        return f"Edge({self.point0},{self.point1})"

    def has_point(self, point: Point):
        """
        Determines if some given Point exists on the Edge.

        Utilizes super().has_point(point) to determine if the Point exists on the Edge's Line. Then, this function
        defines bounds for the Point depending on the ends of the Edge. If the given Point is both on the Edge's Line
        and within the bounds of the Edge, it exists on the Edge.
        :param point: some Point
        :return: True if the point exists on the Edge, False otherwise
        """
        x0 = self.point0.x
        x1 = self.point1.x
        y0 = self.point0.y
        y1 = self.point1.y
        z0 = self.point0.z
        z1 = self.point1.z

        if x0 > x1:
            max_x = x0
            min_x = x1
        else:
            max_x = x1
            min_x = x0

        if y0 > y1:
            max_y = y0
            min_y = y1
        else:
            max_y = y1
            min_y = y0

        if z0 > z1:
            max_z = z0
            min_z = z1
        else:
            max_z = z1
            min_z = z0

        return super().has_point(point) and min_x <= point.x <= max_x and min_y <= point.y <= max_y and \
            min_z <= point.z <= max_z
