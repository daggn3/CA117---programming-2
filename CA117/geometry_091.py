class Shape(object):

	def __init__(self, points):
		self.points = points

	def sides(self):
		l = []
		for i in range(1, len(self.points)):
			l.append(Point.distance(self.points[i], self.points[i - 1]))

		l.append(Point.distance(self.points[-1], self.points[0]))
		return l



	def perimeter(self):
		l = sum(self.sides())
		return l

class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, other):
		return ((other.x - self.x) ** 2 +(other.y - self.y) ** 2) ** 0.5

class Triangle(Shape):
	def __init__(self, points):
		super().__init__(points)


	def area(self):
		sides = self.sides()
		a = sides[0]
		b = sides[1]
		c = sides[2]


		s = (a + b + c) / 2

		return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Square(Shape):
	def __init__ (self, points):
		super().__init__(points)

	def area(self):
		sides = self.sides()
		return (sides[0]) ** 2