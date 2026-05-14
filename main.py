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
		self.bomb_count = 3
		self.bombs = []
		self.bullets = []
		self.alive = True
		self.speed(5)
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
		if self.bomb_count > 0:
			self.bomb_count -= 1
			self.bombs.append(Bomb(self))
	
	def die(self):
		self.speed(0)
		self.ht()
			

class Bomb(Turtle):
	def __init__(self,player):
		super().__init__()
		bomb = Turtle()
		bomb.ht()
		bomb.speed(0)
		bomb.penup()
		bomb.goto(self.xcor(),self.ycor())
		bomb.color(self.player_color)
		bomb.shape("circle")
		bomb.shapesize(5,5)
		bomb.st()

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
		self.speed(5)
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
		self.goto(randint(-230,230),randint(-230,230))
		self.heading(self.towards(target))
		self.speed(5)
		self.st()
	
	def move(self):
		self.forward(5)
		if self.xcor() > 230 or self.xcor() < -230:
			self.setheading(180 - self.heading())
		if self.ycor() > 230 or self.ycor() < -230:
			self.setheading(-self.heading())
		self.heading(self.towards(target))
	
	def remove(self):
		self.speed(0)
		self.ht()

class Target(Turtle):
	def __init__(self):
		super().__init__()
		self.ht()
		self.speed(0)
		self.color("red")
		self.penup()
		self.goto(random.randint(-230,230),random.randint(-230,230))
		self.shape("circle")
		self.st()

	def relocate(self):
		self.ht()
		self.goto(random.randint(-230,230),random.randint(-230,230))
		self.st()


#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")
screen.listen()

playing_area()

player1 = Player(screen,"Left","Right","Up","Down")
player2 = Player(screen,"a","d","w","s")
players = [plyer1,player2]
zombies = []
zombie_amount = 2
spot = Target()

while player1.alive == True and player2.alive == True:
	for player in players:
		player.move()
		if len(player.bullets) > 0:
			for bullet in player.bullets:
				bullet.move()
	if player1.distance(spot) < 20 or player2.distance(spot):
		for player in players:
			for num in zombie_amount:
				zombies.append(Zombie(player))
		zombie_amount += 1
		spot.relocate()
	if len(zombies) > 0:
		for zombie in zombies:
			zombie.move()
			

screen.mainloop()



screen.exitonclick()