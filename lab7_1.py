import math
class Sphere():
    """Class that representing a sphere in a 3-way space"""

    def __init__(self, radius = 1.0, x = 0.0, y = 0.0, z = 0.0):

        """
        Constructor that take a radius of a sphere and 3 coordinates of it centre
        By default all coordinates equals to 0 radius equal to 1.
        """
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z


    def get_center(self):
        """Method thet returns a tuple with given coordinates of center of the sphere """
        return self.x, self.y, self.z



    def get_volume(self):
        """Metod that returns a volume of a sphere"""
        self.volume = 1.333333333333 * math.pi * self.radius ** 3
        return self.volume

    def get_radius(self):
        """Method that returns radius of a sphere"""
        return self.radius

    def get_square(self):
        """Return square of a given sphere """
        self.square = 4 * math.pi * self.radius ** 2
        return self.square

    def is_point_inside(self, a, b, c):

        """Method that checks if point with given coordinates a, b, c is inside of a sphere"""

        if math.sqrt(((self.x - a)**2) + ((self.y - b) ** 2) + ((self.z - c) ** 2)) < self.radius:
            return True
        return False


    def set_radius(self, new_radius):
        """ Set radius of the sphere to a given value"""
        self.radius = new_radius


    def set_center(self, new_x, new_y, new_z):
        """Method that set new coordinates of center of given sphere"""
        self.x = new_x
        self.y = new_y
        self.z = new_z









