import turtle as trtl
import random as Rand

# game screen setup
wn = trtl.Screen()
wn.bgcolor('black')

# Background images
background = "./CSP1/maze3.gif"
wn.addshape(background)
endscreen = './CSP1/end credits.gif'
wn.addshape(endscreen)
Start_Screen = "./CSP1/Start Screen.gif"
wn.addshape(Start_Screen)
Loading = "./CSP1/Loading....gif"
wn.addshape(Loading)
wn.bgpic(Loading)

# pong ball and walls
wall_width, wall_height = .5, 5
border_width, border_height = 80, .5

# pong ball
pong = trtl.Turtle()
pong.ht()
pong.up()
pong.shape('circle')
pong.color('black')
pong.shapesize(float(.5))
pong.speed("fastest")

# paddles and walls
wall4= trtl.Turtle ()
wall4.ht()
wall4.up()
wall4.shape('square')
wall4.shapesize(border_height, border_width)
wall4.goto(525, 0)
wall4.seth(90)
wall4.speed("fastest")

wall3= trtl.Turtle ()
wall3.ht()
wall3.up()
wall3.shape('square')
wall3.shapesize(border_height, border_width)
wall3.goto(-525, 0)
wall3.seth(90)
wall3.speed("fastest")

wall2 = trtl.Turtle()
wall2.ht()
wall2.up()
wall2.shape('square')
wall2.color('blue')
wall2.shapesize(wall_width, wall_height)
wall2.goto(-350, 0)
wall2.seth(90)
wall2.speed("fastest")

wall1 = trtl.Turtle()
wall1.ht()
wall1.up()
wall1.shape('square')
wall1.color('red')
wall1.shapesize(wall_width, wall_height)
wall1.goto(350, 0)
wall1.seth(90)
wall1.speed("fastest")

top_border = trtl.Turtle()
top_border.ht()
top_border.up()
top_border.shape('square')
top_border.shapesize(border_width, border_height)
top_border.goto(0, -300)
top_border.seth(90)
top_border.speed("fastest")

bttm_border = trtl.Turtle()
bttm_border.ht()
bttm_border.up()
bttm_border.shape('square')
bttm_border.shapesize(border_width, border_height)
bttm_border.goto(0, 300)
bttm_border.seth(90)
bttm_border.speed("fastest")

# score counters
scorer1 = trtl.Turtle()
scorer1.ht()
scorer1.up()
scorer1.goto(50, 250)
scorer1.pd()
scorer1.speed("fastest")

scorer2 = trtl.Turtle()
scorer2.ht()
scorer2.up()
scorer2.goto(-150, 250)
scorer2.pd()
scorer2.speed("fastest")

# variables for the game
curser_size = 20
angle = 0
poolean = True
bluescore = 0
redscore = 0
font_setup = ("Arial", 20, "normal")

# move buttons
def up():
    wall1.fd(15)
def LL():
    wall2.fd(15)
def Ln():
    wall2.bk(15)
def dn():
    wall1.bk(15)

# fun buttons
def reset():
    pong.goto(0, 0)
    pong.seth(0)
    wall1.goto(350, 0)
    wall2.goto(-350, 0  )

def bugfix():
    pong.seth(Rand.randint(0, 360))

def funbutton():
    global angle
    global poolean
    global bluescore
    global redscore
    poolean = False
    wall1.st()
    wall2.st()
    pong.st()
    wn.bgpic(background)
    while poolean == False:
        pong.fd(5)
        if paddle_collision(pong, wall1):
            pong.bk(5)
            bugfix()
        if paddle_collision(pong, wall2):
            pong.bk(5)
            bugfix()
        if hrzntl_brdr_colide(pong, top_border):
            pong.bk(5)
            pong.seth(Rand.randint(0, 180))
        if hrzntl_brdr_colide(pong, bttm_border):
            pong.bk(5)
            pong.seth(Rand.randint(-180, 0))
        if scorebordercoll(pong, wall3):
            redscore += 1
            scorer1.clear()
            scorer1.write(redscore, font=font_setup)
            reset()
        if scorebordercoll(pong, wall4):
            bluescore += 1
            scorer2.clear()
            scorer2.write(bluescore, font=font_setup)
            reset()

def stop():
    global poolean
    wn.clear()
    wn.bgpic(endscreen)
    if poolean == True:
        poolean = False
    else:
        poolean = True

def stort():
    wn.bgcolor('black')   
    wall1.st()
    wall2.st()
    pong.st()
    top_border.st()
    run_pong()

# game runs
def run_pong():
    global angle
    global bluescore
    global redscore
    wn.bgpic(background)
    while poolean == True:
        pong.fd(5)
        # detect collisions between the pong ball and the walls
        if paddle_collision(pong, wall1):
            pong.bk(5)
            if pong.ycor() + wall1.ycor() == 0.0:
                angle = 180
                pong.seth(angle)
            else:
                angle = Rand.randint(135, 225)
                pong.seth(angle)
            print(angle)
        if paddle_collision(pong, wall2):
            if angle == 180:
                angle = 0.0
                pong.seth(angle)
            else:
                angle = Rand.randint(-45, 45)
                pong.seth(angle)
            print(angle)
        if hrzntl_brdr_colide(pong, top_border):
            pong.seth(Rand.randint(0, 180))
        if hrzntl_brdr_colide(pong, bttm_border):
            pong.seth(Rand.randint(-180, 0))
        if scorebordercoll(pong, wall3):
            redscore += 1
            scorer1.clear()
            scorer1.write(redscore, font=font_setup)
            reset()
        if scorebordercoll(pong, wall4):
            bluescore += 1
            scorer2.clear()
            scorer2.write(bluescore, font=font_setup)
            reset()

# collision functions
def paddle_collision(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + wall_width/2 and abs(a.ycor() - b.ycor()) < curser_size/2 + wall_height * curser_size

def hrzntl_brdr_colide(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + border_width * curser_size and abs(a.ycor() - b.ycor()) < curser_size/2 + border_height/2

def scorebordercoll(a, b):
    return abs(a.xcor() - b.xcor()) < curser_size/2 + wall_width * curser_size and abs(a.ycor() - b.ycor()) < curser_size/2 + 999/2

# key press sensors
wn.bgcolor('White')
wn.bgpic(Start_Screen)
wn.onkeypress(up,"Up")
wn.onkeypress(dn,"Down")
wn.onkeypress(LL,"w")
wn.onkeypress(Ln,"s") 
wn.onkeypress(bugfix,"slash")
wn.onkeypress(funbutton,"f")
wn.onkeypress(stort, "space")
wn.onkeypress(reset, "r")
wn.onkeypress(stop, "Escape")
wn.listen()
wn.mainloop()