import turtle

class BasicEntities():
	def __init__(self, x, y, speed ):
		self.x = x
		self.y = y
		self.speed = speed
		self.obj = turtle.Turtle()
		self.obj.speed(0)
		self.obj.up()
		self.obj.ht()
		self.obj.setposition(x, y)

class Player(BasicEntities):
	def __init__(self, x, y, speed):
		super().__init__(x, y, speed)
		self.obj.color('red')
		self.obj.shape('circle')
		self.obj.shapesize(7)
		self.speed = speed

	def go_up(self):
		self.y = self.obj.ycor()
		if self.y <= 200:
			self.obj.sety(self.y + self.speed)

	def go_down(self):
		self.y= self.obj.ycor()
		if self.y>= -200:
			self.obj.sety(self.y - self.speed)

	def go_left(self):
		self.x = self.obj.xcor()
		if self.x >= -200:
			self.obj.setx(self.x - self.speed)

	def go_right(self):
		self.x = self.obj.xcor()
		if self.x <= 200:
			self.obj.setx(self.x + self.speed)
		
class CustomButton(BasicEntities):
	def __init__(self, x, y, speed):
		super().__init__(x, y, speed)

	def clic(self, x, y):
		if x > (button_start.obj.xcor() - 75) and x < (button_start.obj.xcor() + 75):
			if y > (button_start.obj.ycor() - 25) and y < (button_start.obj.ycor() + 25):
				button_start.obj.clear()
				red_circle.obj.st()

		if x > (self.obj.xcor() - 50) and x < (self.obj.xcor() + 50):
			if y > (self.obj.ycor() - 25) and y < (self.obj.ycor() + 25):
				turtle.bye()	

	def draw_button_exit(self):
		self.obj.setposition(self.x, self.y)
		self.obj.down()
		self.obj.forward(100)
		self.obj.left(90)
		self.obj.forward(50)
		self.obj.left(90)
		self.obj.forward(100)
		self.obj.left(90)
		self.obj.forward(50)
		self.obj.left(90)	
		self.obj.up()
		self.obj.setposition(-185, -195)
		self.obj.write('EXIT', font = ('Arial', 24, 'normal'))
		self.obj.setposition(-150, -175)

	def draw_button_start(self):
		self.obj.setposition(self.x, self.y)
		self.obj.down()
		self.obj.begin_fill()
		self.obj.forward(150)
		self.obj.left(90)
		self.obj.forward(50)
		self.obj.left(90)
		self.obj.forward(150)
		self.obj.left(90)
		self.obj.forward(50)
		self.obj.left(90)
		self.obj.color('lightgrey')
		self.obj.end_fill()
		self.obj.color('black')
		self.obj.up()
		self.obj.setposition(-50, 5)
		self.obj.write('START', font = ('Arial', 24, 'normal'))
		self.obj.setposition(0, 0)


red_circle = Player(x = 0, y = 0, speed = 20)

button_exit = CustomButton(x = -200, y = -200, speed = 0)
button_exit.draw_button_exit()

button_start = CustomButton(x = -75, y = 0, speed = 0)
button_start.draw_button_start()

turtle.listen()
turtle.onscreenclick(button_exit.clic, 1)
turtle.onkey(red_circle.go_up, 'w')
turtle.onkey(red_circle.go_up, 'W')
turtle.onkey(red_circle.go_left, 'a')
turtle.onkey(red_circle.go_left, 'A')
turtle.onkey(red_circle.go_down, 's')
turtle.onkey(red_circle.go_down, 'S')
turtle.onkey(red_circle.go_right, 'd')
turtle.onkey(red_circle.go_right, 'D')

turtle.done()