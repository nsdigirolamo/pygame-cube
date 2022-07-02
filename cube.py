from math import sqrt, cos, sin, atan2

import pygame

from edge import Edge
from point import Point
from camera import Camera


class Cube:
    """
    Represents a Cube in 3D space.

    Attributes:
        position: Point
            the center point of the Cube
        length: float
            the length of the Cube's faces
    """

    def __init__(self, position: Point, length: float):
        """
        Instantiates a new Cube.

        :param position: the Cube's position
        :param length: the length of the Cube's faces
        """
        self.position = position
        self.length = length
        self.halfLength = self.length / 2
        x = position.x
        y = position.y
        z = position.z
        self.vertices = [
            Point(x + self.halfLength, y + self.halfLength, z + self.halfLength),
            Point(x + self.halfLength, y + self.halfLength, z - self.halfLength),
            Point(x - self.halfLength, y + self.halfLength, z - self.halfLength),
            Point(x - self.halfLength, y + self.halfLength, z + self.halfLength),
            Point(x + self.halfLength, y - self.halfLength, z + self.halfLength),
            Point(x + self.halfLength, y - self.halfLength, z - self.halfLength),
            Point(x - self.halfLength, y - self.halfLength, z - self.halfLength),
            Point(x - self.halfLength, y - self.halfLength, z + self.halfLength)
        ]
        self.edges = [
            # top face
            Edge(self.vertices[0], self.vertices[1]),
            Edge(self.vertices[1], self.vertices[2]),
            Edge(self.vertices[2], self.vertices[3]),
            Edge(self.vertices[3], self.vertices[0]),
            # bottom face
            Edge(self.vertices[4], self.vertices[5]),
            Edge(self.vertices[5], self.vertices[6]),
            Edge(self.vertices[6], self.vertices[7]),
            Edge(self.vertices[7], self.vertices[4]),
            # connecting edges between two faces
            Edge(self.vertices[0], self.vertices[4]),
            Edge(self.vertices[1], self.vertices[5]),
            Edge(self.vertices[2], self.vertices[6]),
            Edge(self.vertices[3], self.vertices[7]),
        ]

    def __repr__(self):
        return f"Cube({self.position},{self.length})"

    def translate(self, x: float, y: float, z: float):
        """
        Translates the Cube through 3D space.
        :param x: the x component of the translation
        :param y: the y component of the translation
        :param z: the z component of the translation
        """
        self.position.x += x
        self.position.y += y
        self.position.z += z

    def rotate_x(self, rotation: float):
        """
        Rotates the Cube about its x axis.

        Converts the cartesian coordinates of the Cube's z and y positions to polar coordinates.
        Adds the rotation to the polar coordinates and then converts back to cartesian coordinates. More info:
        https://brilliant.org/wiki/convert-cartesian-coordinates-to-polar/
        https://brilliant.org/wiki/convert-polar-coordinates-to-cartesian/
        :param rotation: the Cube's rotation in radians
        :return: the rotated Cube
        """
        for vertex in self.vertices:
            x = vertex.z - self.position.z
            y = vertex.y - self.position.y
            # convert to polar coordinates in (r, theta) format and add rotation
            r = sqrt(x ** 2 + y ** 2)
            phi = atan2(y, x) + rotation
            # convert back to cartesian
            x = r * cos(phi)
            y = r * sin(phi)
            vertex.z = x + self.position.z
            vertex.y = y + self.position.y

    def rotate_y(self, rotation: float):
        """
        Rotates the Cube about its y axis.

        Converts the cartesian coordinates of the Cube's x and z positions to polar coordinates.
        Adds the rotation to the polar coordinates and then converts back to cartesian coordinates. More info:
        https://brilliant.org/wiki/convert-cartesian-coordinates-to-polar/
        https://brilliant.org/wiki/convert-polar-coordinates-to-cartesian/
        :param rotation: the Cube's rotation in radians
        :return: the rotated Cube
        """
        for vertex in self.vertices:
            x = vertex.x - self.position.x
            y = vertex.z - self.position.z
            # convert to polar coordinates in (r, theta) format and add rotation
            r = sqrt(x ** 2 + y ** 2)
            phi = atan2(y, x) + rotation
            # convert back to cartesian
            x = r * cos(phi)
            y = r * sin(phi)
            vertex.x = x + self.position.x
            vertex.z = y + self.position.z

    def rotate_z(self, rotation: float):
        """
        Rotates the Cube about its z axis.

        Converts the cartesian coordinates of the Cube's x and y positions to polar coordinates.
        Adds the rotation to the polar coordinates and then converts back to cartesian coordinates. More info:
        https://brilliant.org/wiki/convert-cartesian-coordinates-to-polar/
        https://brilliant.org/wiki/convert-polar-coordinates-to-cartesian/
        :param rotation: the Cube's rotation in radians
        :return: the rotated Cube
        """
        for vertex in self.vertices:
            x = vertex.x - self.position.x
            y = vertex.y - self.position.y
            # convert to polar coordinates in (r, theta) format and add rotation
            r = sqrt(x ** 2 + y ** 2)
            phi = atan2(y, x) + rotation
            # convert back to cartesian
            x = r * cos(phi)
            y = r * sin(phi)
            vertex.x = x + self.position.x
            vertex.y = y + self.position.y


def draw_cube(cube: Cube, camera: Camera, screen: pygame.Surface):
    """
    Draws a Cube on the given Surface
    :param cube: the Cube
    :param camera: the Camera viewing the Cube
    :param screen: the Surface
    """
    for index, edge in enumerate(cube.edges):
        point0 = camera.get_screen_pos(edge.point0, screen.get_width() / 2, screen.get_height() / 2)
        point1 = camera.get_screen_pos(edge.point1, screen.get_width() / 2, screen.get_height() / 2)
        pygame.draw.aaline(screen, (255, 255, 255), point0, point1, 1)
