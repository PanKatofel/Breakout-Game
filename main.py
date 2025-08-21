from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from text import Text
from time import sleep

# ----------------------------------------- SCREEN -----------------------------------------
screen = Screen()
screen.title("Breakout")
screen.setup(1000, 500)
screen.bgcolor("black")
screen.getcanvas().winfo_toplevel().resizable(False, False)


# ----------------------------------------- VARS -----------------------------------------
bricks = []

screen.tracer(0)
for row in range(10):
    for col in range(5):
        brick = Brick(x=-410 + (row * 90), y=col * 40, health=col+1)
        bricks.append(brick)

paddle = Paddle()
ball = Ball()
screen.update()


# ----------------------------------------- METHODS -----------------------------------------
def col_wall():
    if ball.xcor() >= (screen.window_width() / 2) - 10 or ball.xcor() <= -(screen.window_width() / 2) + 10:
        ball.horizontal_bounce()

    if ball.ycor() >= (screen.window_height() / 2) - 15:
        ball.vertical_bounce()


def col_paddle():
    if abs(paddle.xcor() - ball.xcor()) <= (paddle.WIDTH + ball.RADIUS) / 2 and abs(paddle.ycor() - ball.ycor()) <= (paddle.HEIGHT + ball.RADIUS) / 2:
        offset = ball.xcor() - paddle.xcor()
        ball.paddle_bounce_off(offset)


def col_brick():
    if ball.hit_cooldown:
        return

    for brick_obj in bricks[:]:
        if abs(brick_obj.xcor() - ball.xcor()) <= (brick_obj.WIDTH + ball.RADIUS) / 2 and abs(brick_obj.ycor() - ball.ycor()) <= (brick_obj.HEIGHT + ball.RADIUS) / 2:
            print(abs(brick_obj.xcor() - ball.xcor()))
            print()

            ball.brick_bounce_off(brick_obj)
            ball.hit_cooldown = True
            ball.speed_up()

            brick_obj.hit()
            if not brick_obj.alive:
                bricks.remove(brick_obj)

            screen.ontimer(ball.reset_cooldown, 150)
            break

def col_void():
    if ball.ycor() <= -(screen.window_height() / 2):
        return True


def game_update():
    if paddle.right:
        paddle.move_right()
    elif paddle.left:
        paddle.move_left()

    col_wall()
    col_paddle()
    col_brick()
    ball.move()

    if col_void():
        Text("Game Over")
        screen.ontimer(screen.bye, 3000)
        return

    if len(bricks) <= 0:
        Text("Game Won")
        screen.ontimer(screen.bye, 3000)
        return

    screen.update()

    screen.ontimer(game_update, 15)


# ----------------------------------------- EVENTS -----------------------------------------
game_update()

screen.listen()
screen.onkeypress(paddle.press_right, "Right")
screen.onkeyrelease(paddle.release_right, "Right")
screen.onkeypress(paddle.press_left, "Left")
screen.onkeyrelease(paddle.release_left, "Left")


screen.mainloop()
