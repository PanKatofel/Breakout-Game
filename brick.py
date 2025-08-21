from turtle import Turtle


class Brick(Turtle):

    WIDTH = 80
    HEIGHT = 10

    def __init__(self, x, y, health):
        super().__init__()
        self.health = health
        self.alive = True

        self.setup(x, y)
        self.set_color_by_health()

    def setup(self, x, y):
        self.penup()
        self.speed("fastest")
        self.goto(x, y)
        self.shape("square")
        self.color("white")
        self.shapesize(self.HEIGHT / 20, self.WIDTH / 20)

    def hit(self):
        self.health -= 1
        self.set_color_by_health()

    def set_color_by_health(self):
        match self.health:
            case 5:
                self.color("red")
            case 4:
                self.color("orange")
            case 3:
                self.color("yellow")
            case 2:
                self.color("green")
            case 1:
                self.color("blue")
            case _:
                self.destroy()

    def destroy(self):
        self.hideturtle()
        self.alive = False
        self.goto(1000, 1000)
