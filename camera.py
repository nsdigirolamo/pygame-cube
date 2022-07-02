from edge import Edge
from plane import Plane
from point import Point
from vector import Vector


class Camera:
    def __init__(self, pos: Point, viewport_dist: float):
        """
        Instantiates a new Camera.

        :param pos: the Camera's position
        :param viewport_dist: the distance from the Cube to its viewing frame.
        """
        self.position = pos

        # right now the camera can only face towards positive x
        direction = Vector(1, 0, 0)
        self.direction = direction.get_unit_vector()

        self.viewportDistance = viewport_dist
        frame_x_pos = self.position.x + self.direction.x * self.viewportDistance
        frame_y_pos = self.position.y + self.direction.y * self.viewportDistance
        frame_z_pos = self.position.z + self.direction.z * self.viewportDistance
        self.viewport = Plane(Point(frame_x_pos, frame_y_pos, frame_z_pos), self.direction)

    def __repr__(self):
        return f"Camera(position:{self.position}, direction:{self.direction}, " \
               f"viewportDistance:{self.viewportDistance}, viewport:{self.viewport})"

    def get_screen_pos(self, point: Point, center_x: float, center_y: float):
        """
        Calculates the 2D position on a screen of a given 3D point.

        :param point: the given point
        :param center_x: the horizontal center of the screen
        :param center_y: the vertical center of the screen
        """
        sight_line = Edge(self.position, point)
        intersect = self.viewport.get_intersection(sight_line)
        if intersect is not None:
            return center_x + intersect.y, center_y + intersect.z
        else:
            return None



