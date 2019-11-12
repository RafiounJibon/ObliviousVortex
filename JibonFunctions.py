import turtle
turtle.colormode(255)
bob=turtle.Turtle()
bob.speed(0)
turtle.bgcolor("black")

def design4():
    for times in range(360):
        colors=["red","blue","green","orange","yellow","purple"]
        turtle.pencolor(colors[times%5])
        turtle.width(times/100+1)
        turtle.forward(150)
        turtle.left(59)


def design3():
    turtle.tracer(False)
    for times in range(255):
        bob.pu()
        bob.forward(times)
        bob.left(10)
        bob.pd()
        polygon(3,40,(255-times,0,0))
        bob.color((c,0,0))
        bob.stamp()
    turtle.tracer(True)

def design2():
    for times in range(360):
        colors=["red","purple","orange","purple","red","blue"]
        turtle.width(times/100+1)
        turtle.forward(times)
        turtle.left(59)

def design1():
    for times in range(360):
        colors=["red","purple","orange","purple","red","blue"]
        turtle.pencolor(colors[times%5])
        turtle.width(times/100+1)
        turtle.forward(times)
        turtle.left(70)
    
def spikeflower(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 4)

def spikeflower2(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 4)
        bob.color(c,0,0)
        
def spikeflower3(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times * 4)
        bob.color(0,0,c)

def spikeflower4(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times *10 )
        bob.color(0,c,0)

def spike5(distance):
    for times in range(11):
        c = times * 12
        bob.color(c,c,0)
        bob.width(times*1.05)
        bob.forward(distance)
        bob.left(10)

def spike4(distance):
    for times in range(11):
        c = times * 12
        bob.color(0,0,c)
        bob.width(times*1.05)
        bob.forward(distance)
        bob.left(10)

def spike3(distance):
    for times in range(11):
        c = times * 12
        bob.color(0,c,0)
        bob.width(times*1.05)
        bob.forward(distance)
        bob.left(10)

def spike2(distance):
    for times in range(11):
        c = times * 12
        bob.color(c,0,0)
        bob.width(times*1.05)
        bob.forward(distance)
        bob.left(10)
        
def vortex(distance):
    for times in range(11):
        c = times * 12
        bob.color(c,0,c)
        bob.width(times*1.05)
        bob.forward(distance)
        bob.left(10)

def tile(c):
    for times in range(4):
        polygon(3, 50, "black")
        bob.forward(50)
        polygon(3, 50, "black")
        bob.forward(50)
        polygon(3, 50, "black")
        bob.forward(50)
        polygon(3, 50, "black")
        bob.forward(50)
        bob.left(90)

def rowtile(c):
    for times in range(8):
        tile(c)
        bob.forward(200)

def square(distance):
    for times in range(4):
        bob.forward(distance)
        bob.left(90)

def triangle(distance):
    for times in range(3):
        bob.forward(distance)
        bob.left(120)

def pentagon(distance):
    sides=5
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

def polygon(sides,distance,c):
    bob.color(c)
    angle= 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance, c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

def explosion(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)
    bob.end_fill()

def figure1(distance,size,c):
    bob.color(c)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    bob.forward(distance)
    bob.circle(size)

def monster(color):
    bob.color(color)
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(135)
    bob.forward(35)
    bob.right(90)

def fadingTriangle():
    for times in range(50):
        c = (250 - times * 5, 250 - times * 5, 0)
        polygon(3, 450 - times * 8,c)
        
