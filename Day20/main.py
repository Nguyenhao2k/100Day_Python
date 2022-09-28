from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend_segment()
        score.increaseScore()
        
    
    
    #Dectect collision with wall.
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        game_is_on = False
        score.game_over()
    
    #Dectec collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()
        


screen.exitonclick()