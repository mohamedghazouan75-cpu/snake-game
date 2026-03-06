import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

window = Screen()
window.setup(800,800)
window.bgcolor('black')
window.tracer(0)

sam = Snake()
food = Food()
score = Scoreboard()

game_on = True
while game_on:
    sam.move_snake()
    window.update()
    time.sleep(0.15)
    window.listen()
    window.onkey(sam.up,'Up')
    window.onkey(sam.down,'Down')
    window.onkey(sam.right,'Right')
    window.onkey(sam.left,'Left')
    
    if sam.head.distance(food)<20:
        food.appear()
        sam.extend()
        score.increase_score()
    for segment in sam.turtles[0:-1]:
        if sam.head.distance(segment) <10:
            game_on =False
            score.game_over()
    
    if sam.head.xcor()>390 or sam.head.xcor()<-390 or sam.head.ycor()>400 or sam.head.ycor()<-390:
        game_on = False
        score.game_over()



window.exitonclick()