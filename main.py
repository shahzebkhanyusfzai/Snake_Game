import time
import turtle
from snake import Snake
from food import Food
from score import Score
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)

cobra = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(cobra.up,"Up")   
screen.onkey(cobra.down,"Down")
screen.onkey(cobra.left,"Left")
screen.onkey(cobra.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    cobra.move()
    if cobra.head.distance(food)<15:
        food.refresh()
        cobra.extend()
        score.cobra_score()


    # Detecting collision
    if cobra.head.xcor()>280 or cobra.head.xcor()<-280 or cobra.head.ycor()>280 or cobra.head.ycor()<-280:
        game_is_on = False 
        score.gameover()

    for s in cobra.seg:
        if s == cobra.head:
            pass
        elif cobra.head.distance(s)<10:
            game_is_on = False 
            score.gameover()            
           

screen.exitonclick()