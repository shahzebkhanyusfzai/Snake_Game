
import turtle
from turtle import Turtle
starting_pos = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self): 
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]


    def create_snake(self):

            for pos in starting_pos:
                new_seg = Turtle("square")
                new_seg.color("white")
                new_seg.penup()
                new_seg.goto(pos)
                self.seg.append(new_seg)

    def add_segment(self,pos):
        self.new_segment = Turtle("square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(pos)
        self.seg.append(self.new_segment)
    
    def move(self):
        for x in range(len(self.seg)-1,0,-1):
            new_x = self.seg[x-1].xcor()
            new_y = self.seg[x-1].ycor()
            self.seg[x].goto(new_x,new_y)

        self.head.forward(20)

    def extend(self):
        self.add_segment(self.seg[-1].position())


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)