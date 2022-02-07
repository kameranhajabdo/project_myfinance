import math


class GeometricalForm:
    def __init__(self, lines: list[float]):
        self.lines = lines

    def perimiter(self):
        return sum(self.lines)



class Triangle(GeometricalForm):
    def __init__(self, line1: float, line2: float, line3: float):
        super().__init__([line1, line2, line3])


    def area(self):
        sp = self.perimeter() / 2
        return math.sqrt(sp *(sp - self.lines[0]) * (sp - self.line[1]) * (sp - self.line[2]))


class Rectangle(GeometricalForm):
    def __init__(self, length: float , width: float):
        super().__init__([length, width, length, width])

    def perimeter(self) -> float:
        return self.length * 2 + self.width * 2

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, line :float):
        super().__init__(line, line)


if __name__ == "__main__":
    t = Triangle(2, 3 , 5)
    print("triangle p", t.perimeter())
    print("triangle area", t.area())
    d = Rectangle(5, 7)
    print("rectangle p", d.perimeter())
    print("rectangle area", d.area())
    s = Square(1)
    print("square p", s.perimeter())
    print("square area", s.area())