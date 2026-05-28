from turtle import *
from random import randint, choice
import time

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
	def __init__(self,screen,color,left_key,right_key,fire_key,bomb_key):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.color(color)
		self.player_color = color
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
		self.bullets = []
		self.bombs = []
		self.ht()
			
class Bomb(Turtle):
	def __init__(self,player):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.goto(player.xcor(),player.ycor())
		self.color(player.player_color)
		self.shape("circle")
		self.start = time.time()
		self.st()

	def explode(self,zombies):
		if time.time() - self.start > 1:
			self.shapesize(10,10)
			for zombie in zombies:
				if zombie.distance(self) <= 100:
					zombie.die(zombies)
			if time.time() - self.start > 2:
				self.ht()
				player.bombs.remove(self)

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
			self.speed(0)
			self.ht()
			self.player.bullets.remove(self)

class Zombie(Turtle):
	def __init__(self,target,zombies):
		super().__init__()
		self.ht()
		self.speed(0)
		self.penup()
		self.color("green")
		self.shape("turtle")
		self.target = target
		self.goto(randint(-230,230),randint(-230,230))
		self.setheading(self.towards(target))
		self.speed(5)
		self.st()
	
	def move(self):
		self.forward(5)
		if self.xcor() > 230 or self.xcor() < -230:
			self.setheading(180 - self.heading())
		if self.ycor() > 230 or self.ycor() < -230:
			self.setheading(-self.heading())
		self.setheading(self.towards(self.target))
	
	def die(self,zombies):
		self.speed(0)
		self.ht()
		zombies.remove(self)

class Target(Turtle):
	def __init__(self):
		super().__init__()
		self.ht()
		self.speed(0)
		self.color("red")
		self.penup()
		self.goto(randint(-230,230),randint(-230,230))
		self.shape("circle")
		self.st()

	def relocate(self):
		self.ht()
		self.goto(randint(-230,230),randint(-230,230))
		self.st()

class Score(Turtle):
	def __init__(self,x,y,screen,p_num,score):
		super().__init__()
		self.ht()
		self.penup()
		self.score = score
		self.p_num = p_num
		self.goto(x,y)
		self.color("White")
	
	def update_score(self):
		self.clear()
		str_score = str(self.score)
		self.write("Player "+self.p_num+"'s score is: "+str_score,font=("Arial",12))


#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")
screen.listen()

playing_area()
start = time.time()

player1 = Player(screen,generate_color(),"Left","Right","Up","Down")
player2 = Player(screen,generate_color(),"a","d","w","s")
players = [player1,player2]

score1 = Score(-250, 265,screen,"One",0)
score2 = Score(90, 265,screen,"Two",0)

zombies = []
zombie_amount = 2
spot = Target()

finish = Turtle()
finish.ht()
finish.penup()
finish.goto(-70,0)
finish.color("Black")

while len(players) > 1:
	for player in players:
		player.move()
		if len(player.bullets) > 0:
			for bullet in player.bullets:
				bullet.move()
				if len(zombies) > 0:
					for zombie in zombies:
						if zombie.distance(bullet) < 20:
							zombie.die(zombies)
							bullet.remove()
							if player == player1:
								score1.score += 1
								score1.update_score()
							elif player == player2:
								score2.score += 1
								score2.update_score()
		if len(player.bombs) > 0:
			for bomb in player.bombs:
				bomb.explode(zombies)
	if player1.distance(spot) < 20 or player2.distance(spot) < 20:
		for player in players:
			for num in range(zombie_amount):
				zombies.append(Zombie(player,zombies))
		zombie_amount += 1
		spot.relocate()
	if len(zombies) > 0:
		for zombie in zombies:
			zombie.move()
			if zombie.distance(zombie.target) < 20:
				if zombie.target == player1:
					player1.die()
					players.remove(player1)
				elif zombie.target == player2:
					player2.die()
					players.remove(player2)

if player1 in players:
	finish.write("Player 1 Wins!",font=("Arial",20))
elif player2 in players:
	finish.write("Player 2 Wins!",font=("Arial",20))
					
	

			

screen.mainloop()



screen.exitonclick()