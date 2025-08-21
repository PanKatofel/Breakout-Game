from turtle import Turtle
from random import randint


class Ball(Turtle):

    SPEED = 7
    RADIUS = 15

    def __init__(self):
        super().__init__()

        self.hit_cooldown = False
        self.setup()

    def setup(self):
        self.penup()
        self.goto(0, -85)
        self.shape("circle")
        self.color("white")
        self.shapesize(self.RADIUS / 20, self.RADIUS / 20)
        self.setheading(randint(20, 80))
        self.speed("fastest")

    def move(self):
        self.forward(self.SPEED)

    def vertical_bounce(self):
        self.setheading((360 - self.heading()) % 360)

    def horizontal_bounce(self):
        self.setheading((180 - self.heading()) % 360)

    def paddle_bounce_off(self, offset):
        normalized_offset = offset / 100
        angle = normalized_offset * 45
        new_heading = 90 - angle
        self.setheading(new_heading)

    def brick_bounce_off(self, brick):
        if self.xcor() - (self.RADIUS / 2) >= brick.xcor() + (brick.WIDTH / 2) or self.xcor() + (self.RADIUS / 2) <= brick.xcor() - (brick.WIDTH / 2):
            self.horizontal_bounce()
        else:
            self.vertical_bounce()

    def reset_cooldown(self):
        self.hit_cooldown = False

    def speed_up(self):
        self.SPEED += 0.01
