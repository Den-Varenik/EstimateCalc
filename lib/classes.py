from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, shape_id):
        self._shape_id = shape_id

    @property
    def shape_id(self):
        return self._shape_id

    @abstractmethod
    def calc_S(self):
        pass


class Circle(Shape):

    def __init__(self, shape_id, radius: float):
        super(Circle, self).__init__(shape_id)
        self._radius = radius

    def calc_S(self):
        from math import pi
        return pi*self._radius**2


class Square(Shape):

    def __init__(self, shape_id, side: float):
        super(Square, self).__init__(shape_id)
        self._side = side

    def calc_S(self):
        return self._side**2


class Rectangle(Shape):

    def __init__(self, shape_id, side_a: float, side_b: float):
        super(Rectangle, self).__init__(shape_id)
        self._side_a = side_a
        self._side_b = side_b

    def calc_S(self):
        return self._side_a*self._side_b


class Triangle(Shape):

    def __init__(self, shape_id, side_a: float, side_b: float, side_c: float):
        super(Triangle, self).__init__(shape_id)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def calc_S(self):
        num_max = max(self._side_a, self._side_b, self._side_c)
        if num_max < sum([self._side_a, self._side_b, self._side_c]) - num_max:
            from math import sqrt
            p = (self._side_a*self._side_b*self._side_c)/2
            return sqrt(p*(p-self._side_a)*(p-self._side_b)*(p-self._side_c))
        else:
            return 'Треугольник не существует!'
