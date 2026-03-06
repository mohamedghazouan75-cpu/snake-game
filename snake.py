from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtles = []
        self.x_positons = [0,20,40,60]
        self.creat_snake()
        self.head = self.turtles[-1]
    def creat_snake(self):
        for x in range(len(self.x_positons)):
          new_turtle =Turtle('square')
          new_turtle.color('white')
          new_turtle.penup()
          new_turtle.goto(self.x_positons[x],0)
          self.turtles.append(new_turtle)
          
    def move_snake(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.color('red')
        self.head.forward(20)
    
    def extend(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.pu()
        self.turtles.insert(0,new_segment)
        #insert(index, element)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)
    
    def right(self):
        self.head.setheading(0)
    
    def left(self):
        self.head.setheading(180)     