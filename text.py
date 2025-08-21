from turtle import Turtle


class Text(Turtle):

    def __init__(self, message):
        super().__init__()
        self.setup()

        self.write(message, align="center", font=("Arial", 90, "bold"))

    def setup(self):
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 0)
        self.color("white")
