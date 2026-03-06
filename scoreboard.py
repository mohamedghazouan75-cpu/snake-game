from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_scorebord()

    def update_scorebord(self):  
        self.write(f'Score: {self.score}',align = 'center',font = ('Arial',24,'normal'))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorebord()
    
    def game_over(self):
        self.screen.bgcolor('darkred')
        self.goto(0,0)
        self.write(f'GAME OVER\nfinal score: {self.score}',
                   align = 'center',font = ('Arial',24,'normal'))