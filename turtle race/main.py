"""turtle race application"""
from turtle import Turtle, Screen
import random
import turtle as t
#============================================================
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet" , prompt="Which turtle will win the race? Enter a color: ")
colors = ["red" , "orange" , "yellow" , "green" , "blue" , "purple"]
y_positions = [-150 , -100 , -50 , 50 , 100 , 150]
all_turtles = []
#=============================================================================================================
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)
#==============================================================================================================
is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    # turtle size is 40x40 therefore if we write a consition to stop in 250. its alreay exceeds  
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
#==========================================================================================================
screen.exitonclick()