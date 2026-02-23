from turtle import Screen
from snake import Snake

window = Screen()
window.setup(800,800)
window.bgcolor('black')
window.title('Snake Game')

sam = Snake()
while True:
    sam.move_snake()
    window.listen()
    window.onkey(sam.up,'Up')
    window.onkey(sam.down,'Down')
    window.onkey(sam.right,'Right')
    window.onkey(sam.left,'Left')

    


window.exitonclick()