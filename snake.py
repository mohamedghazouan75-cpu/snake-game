from turtle import Turtle
class Snake:
    def __init__(self):
        self.x_positions = [-40,-20,0,20]
        self.turtles =[ ]
        self.creat_snake()
    def creat_snake(self):
        for i in range(len(self.x_positions)):
          new_turtle = Turtle('square')
          new_turtle.color('white')
          new_turtle.penup()
          new_turtle.goto(self.x_positions[i],0)
          self.turtles.append(new_turtle)
    def move_snake(self):
        for x in range(len(self.turtles)-1):
            self.turtles[x].goto(self.turtles[x+1].pos())
        self.turtles[-1].forward(15)
    
    def up(self):
        self.turtles[-1].setheading(90)
    
    def down(self):
        self.turtles[-1].setheading(270)
    
    def right(self):
        self.turtles[-1].setheading(0)
    
    def left(self):
        self.turtles[-1].setheading(180)