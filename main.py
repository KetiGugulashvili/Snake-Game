import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

speed = 0.1

while True:
    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 20:
        snake.increase_by_one()
        food.change_position()
        scoreboard.increase_score()
        speed -= 0.005

    if snake.head.xcor() > 295 or snake.head.ycor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295:
        scoreboard.game_over()
        break

    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.game_over()
            break

screen.exitonclick()