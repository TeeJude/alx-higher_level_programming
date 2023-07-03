#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """This represents a rectangle object."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        area = (self.__width * self.__height)
        return (area)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        perimeter = ((self.__width * 2) + (self.__height * 2))
        return (perimeter)

    def __str__(self):
        """Return the representation of the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec_diag = []
        for i in range(self.__height):
            [rec_diag.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec_diag.append("\n")
        return ("".join(rec_diag))

    def __repr__(self):
        """Return string representation of rectangle to recreate instance."""
        rec_diag = "Rectangle(" + str(self.__width)
        rec_diag += ", " + str(self.__height) + ")"
        return (rec_diag)

    def __del__(self):
        """Print message "Bye rectangle..." when a rectangle is deleted."""
        print("Bye rectangle...")
