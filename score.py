from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.zero = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,280)
        self.myscore = f"score = {self.zero}"
        self.write(self.myscore, move=False, align="center", font=("Arial", 13, "bold"))

    def cobra_score(self):
        self.clear()
        self.zero+=1
        self.myscore = f"score = {self.zero}"
        self.write(self.myscore, move=False, align="center", font=("Arial", 13, "bold"))

    
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=("Arial", 13, "bold"))
