from turtle import *
from random import randint, choice

#### CLASS AND FUNCTION DEFINITIONS #####
def playing_area():
	t = Turtle()
	t.speed(0)
	t.ht()
	t.pu()
	t.goto(-250,250)
	t.color("light blue")
	t.pd()
	t.begin_fill()
	for i in range(4):
		t.forward(500)
		t.right(90)
	t.end_fill()

'''
Player() Class

Constructor( def __init__(self)):
- player should be shaped like a turtle.
- will take in the x and y coordinates for where the player will initially appear.
- will take in a color for the player
- will take in keys to turn left, turn right and shoot bullets.
- player will have an attribute that is a list that stores bullets


move(self):
- moves object forward five pixels

fire(self):
- creates a Bullet object
- appends the Bullet object to the players's bullet list
'''
class Player(Turtle):
	def __init__(self,screen,left_key,right_key,fire_key,x,y):
		self.speed(0)
		self.ht()
		self.penup()
		self.goto(x,y)
		self.shape("turtle")
		self.bullets = []
		screen.onkeypress(self.rt(),right_key)
		screen.onkeypress(self.lt(),left_key)
		screen.onkeypress(self.fire(),fire_key)
	
	def rt(self):
		self.rt(2)

	def lt(self):
		self.lt(2)

	def move(self):
		self.forward(5)

	def fire(self):
		pass



'''
Bullet() Class
Constructor ( def __init__(self) ):
- Input: player object
- Attributes:
	- Position: same as player
	- Heading: same as player
	- Player: the player
 
move(self):
- move 15 or more pixels forward
- should call on the die() method when the bullet leaves the playing area

die()
- hides the object. 
- removes object from the player's bullet list
'''


#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")
screen.listen()

playing_area()

player1 = Player(screen,"Left","Right","Up",10,10)

while True:
	pass

screen.mainloop()
