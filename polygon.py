import turtle

class Polygon:
    def __init__(self,shape, name, size=100):
        self.shape = shape
        self.name = name
        self.size = size
        self.interior_angles = (self.shape-2)*180
        self.angle = self.interior_angles/self.shape

    def draw(self):
        for i in range(self.shape):
            turtle.forward(self.size)
            turtle.right(180-self.angle)
        turtle.done()

class Square(Polygon):
    def __init__(self):
        super().__init__(4, "square, 50")

square = Square()

print(square.shape)
square.draw()


#Pentagon = Polygon(5, "pentagon")
#hexagon = Polygon(6, "hexagon", 50)
#square = Polygon(4, "square")


#print(Pentagon.interior_angles)
#print(hexagon.angle)

#hexagon.draw()