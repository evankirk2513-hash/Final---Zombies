from turtle import *
from random import randint, choice

def generate_color():
    return f"#{randint(0, 0xFFFFFF):06x}"

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

class Player(Turtle):
	def __init__(self,screen,left_key,right_key,fire_key,bomb_key):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.color(generate_color())
		self.goto(randint(-230,230),randint(-230,230))
		self.shape("turtle")
		self.bombs = 3
		self.bullets = []
		self.alive = True
		self.st()
		screen.onkeypress(self.turn_right,right_key)
		screen.onkeypress(self.turn_left,left_key)
		screen.onkeypress(self.fire,fire_key)
		screen.onkey(self.bomb,bomb_key)
	
	def turn_right(self):
		self.rt(10)

	def turn_left(self):
		self.lt(10)

	def move(self):
		self.forward(5)
		if self.xcor() > 230 or self.xcor() < -230:
			self.setheading(180 - self.heading())
		if self.ycor() > 230 or self.ycor() < -230:
			self.setheading(-self.heading())

	def fire(self):
		self.bullets.append(Bullet(self))
	
	def bomb(self):
		self.bombs -= 1
		bomb = Turtle()
		bomb.ht()
		bomb.speed(0)
		bomb.penup()
		bomb.goto(self.xcor(),self.ycor())
		bomb.color(self.player_color)
		bomb.shape("circle")
		bomb.shapesize(5,5)

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(player.player_color)
        self.penup()
        self.setheading(player.heading()) 
        self.goto(player.xcor(),player.ycor())
        self.forward(10)
        self.player = player
        self.st()
    
    def move(self):
        self.forward(15)
        if self.xcor() > 230 or self.xcor() < -230:
            self.remove()
        if self.ycor() > 230 or self.ycor() < -230:
            self.remove()
    
    def remove(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullets.remove(self)

class Zombie(Turtle):
	def __init__(self,target):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.color("green")
		self.shape("turtle")
		self.heading(self.towards(target))

#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")
screen.listen()

playing_area()

player1 = Player(screen,"Left","Right","Up","Down")

while True:
	pass

screen.mainloop()



screen.exitonclick()