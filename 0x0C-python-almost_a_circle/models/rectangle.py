#!/usr/bin/python3

"""The Rectangle Class"""

from models.base import Base

class Rectangle(Base):
    """Recatangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({:d}){:d}/{:d} - {:d}/{:d}".format(self.id, 
                self.__x,
                self.__y,
                self.__width,
                self.__height)
    
    @property
    def width(self):
        """definition of width"""
        return self.__width

    @property
    def height(self):
        """definition of height"""
        return self.__height

    @property
    def x(self):
        """definition of x"""
        return self.__x
    
    @property
    def y(self):
        """definition of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setting the int value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setting the height of the Rectangle"""
        if type(value) is not int:
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("must be >= o")
        self.__height = value

    @x.setter
    def x(self, value):
        """Seting the value of x as int"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setting the value of y to int"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__y = value

    def area(self):
        """Area of the resctangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with #s"""
        for n in range(self.__y):
            print("")
        for row in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """update the attributes with provided values"""
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
            

    def to_dictionary(self):
        """return the dictionary sel"""
        return dict(id=self.id, width=self.width, height=self.height, x=self.x, y=self.y)
