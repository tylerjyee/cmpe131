class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    def draw(self):
        return " "
class Circle():
    def __init__(x, y, size):
        super().__init__(x,y,size)
        def draw(self):
            return f"""
            ({self.x}, {self.y})
            {self.size}
               ,~ ~ ~,
             ,'       ',
             ',       ,'
               ',___,'
            """
class Square(Base):
    def __init__(self, y, size):
        super().__init__(x,y,size)
    def draw():
        return f"""
        ({self.x}, {self.y})
        {self.size}
        --------------------
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
        |                   |
        --------------------
        """
# All of the code below is correct
def draw_any_shape(myShape):
    print(myShape.draw())
def main():
    s = Square(1,2,3)
    draw_any_shape(s)
    c = Circle(2,2,1)
    draw_any_shape(c)
main()