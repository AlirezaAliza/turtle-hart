from inspect import EndOfBlock
from turtle import * 
speed(0)
colors_list = ["blue", "red", "white" , "yellow"]
for i in range(100):
    pencolor(colors_list[i%4])
    color("red")
    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50 , 200)
    right(140)
    circle(50 , 200)
    forward(133)
    end_fill()
    right(5)
done()