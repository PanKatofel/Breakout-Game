from turtle import Turtle


class Paddle(Turtle):

    SPEED = 7.5
    WIDTH = 200
    HEIGHT = 10

    def __init__(self):
        super().__init__()

        self.left = False
        self.right = False
        self.setup()

    def setup(self):
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(self.HEIGHT / 20, self.WIDTH / 20)
        self.goto(0, -170)
        self.color("white")

    def move_left(self):
        if self.xcor() - (self.WIDTH / 2) > -500:
            self.goto(self.xcor() - self.SPEED, self.ycor())

    def move_right(self):
        if self.xcor() + (self.WIDTH / 2) < 500:
            self.goto(self.xcor() + self.SPEED, self.ycor())

    def press_right(self):
        self.right = True

    def release_right(self):
        self.right = False

    def press_left(self):
        self.left = True

    def release_left(self):
        self.left = False
