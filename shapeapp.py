## This was wrote in Python 3 ##
from turtle import *
from time import *
turtle = Turtle()
screen = Screen()

q1 = input("What shape should I draw? The possible shapes are ; Square, Circle, Triangle")

if q1 == "Square":
	turtle.forward(90)
	turtle.right(90)
	turtle.forward(90)
	turtle.right(90)
	turtle.forward(90)
	turtle.right(90)
	turtle.forward(90)
	turtle.right(90)
	asktostop = input("PRESS ENTER WHEN YOU WANT THIS TO CLOSE")
	wait(1)
	print("Ending....")
	wait(3)
	quit()

else:
	print("Sorry, I dont know that one")
	print("Closing in 3 seconds")
	wait(3)
	quit()
