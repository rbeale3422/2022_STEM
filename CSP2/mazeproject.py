import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.screensize(500,300,"black")
wn.title("Turtle Maze Game")

#initialize turtle
mazedrawer = trtl.Turtle()
mazerunner = trtl.Turtle(shape="turtle")

mazerunner.penup()
mazerunner.goto(-60,40)
mazerunner.color("red")
mazerunner.pendown()

counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-500,380)
counter.pendown()
counter.color("white")
timer = 55
counter_interval = 1000   #1000 represents 1 second
timer_up = False


font_setup = ("Arial", 20, "normal")
score = 0
scorekeeper =  trtl.Turtle()
scorekeeper.penup()
scorekeeper.hideturtle()
scorekeeper.goto(400,380)
scorekeeper.pendown()
scorekeeper.color("white")
scorekeeper.write("Score: 0", font=font_setup)


pellet1 = trtl.Turtle(shape="circle")
pellet1.color("red")
pellet2 = trtl.Turtle(shape="circle")
pellet2.color("blue")
pellet3 = trtl.Turtle(shape="circle")
pellet3.color("green")
pellet4 = trtl.Turtle(shape="circle")
pellet4.color("yellow")
pellet5 = trtl.Turtle(shape="circle")
pellet5.color("pink")
pellet6 = trtl.Turtle(shape="circle")
pellet6.color("purple")
pellet7 = trtl.Turtle(shape="circle")
pellet7.color("orange")
pellet8 = trtl.Turtle(shape="circle")
pellet8.color("brown")
pellet9 = trtl.Turtle(shape="circle")
pellet9.color("white")
pellet10 = trtl.Turtle(shape="circle")
pellet10.color("lime")

pellet1.penup()
pellet1.goto(140, 80)

pellet2.penup()
pellet2.goto(-180, 50)

pellet3.penup()
pellet3.goto(-240, -180)

pellet4.penup()
pellet4.goto(220, 190)

pellet5.penup()
pellet5.goto(-260, 80)

pellet6.penup()
pellet6.goto(0,200)

pellet7.penup()
pellet7.goto(170,-180)

pellet8.penup()
pellet8.goto(-190,280)

pellet9.penup()
pellet9.goto(-300,160)

pellet10.penup()
pellet10.goto(100,-90)

#Variables
angle = 90
path_width = 20
wall_length = path_width
# colors = ["blue","red","orange","pink","green","purple","black","brown","goldenrod","sienna","fuchsia"]
wall_thickness = 3
num_walls = 30
mze_wll_clr = "blue"
pixel_size = 20 

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    mazerunner.penup()
    mazerunner.hideturtle()
    wn.onkeypress(None, 'space')
    return
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


def draw_door(pos):
    #draw door
    mazedrawer.forward(pos)
    mazedrawer.penup()
    mazedrawer.forward(path_width*2)
    mazedrawer.pendown()

def draw_barrier(pos):
    #draw barrier
    mazedrawer.forward(pos)
    mazedrawer.left(angle)
    mazedrawer.forward(path_width*2)
    mazedrawer.backward(path_width*2)
    mazedrawer.right(angle)

def go_up():
    mazerunner.setheading(90)
def go_down():
    mazerunner.setheading(270)
def go_left():
    mazerunner.setheading(180)
def go_right():
    mazerunner.setheading(0)            

#Collision for pellets
def pixelCollision(t1,t2):
    global score
    t1_x = t1.xcor()
    t1_y = t1.ycor()
    t2_x = t2.xcor()
    t2_y = t2.ycor()
    if (abs(t1_x- t2_x) < pixel_size) and (abs(t1_y- t2_y) < pixel_size):
        score += 1
        scorekeeper.clear()
        scorekeeper.write("Score: " + str(score), font=font_setup)
        t2.hideturtle()
        t2.goto(400,375)
        if (score == 4):
            scorekeeper.clear()
            scorekeeper.write("You win!", font=font_setup)
            mazerunner.penup()
            mazerunner.hideturtle()
            wn.onkeypress(None, 'space')
            return

def go_turtle():

    mazerunner.forward(1)
    wn_canvas = wn.getcanvas()
    x,y = mazerunner.position()
    margin = 5
    items = wn_canvas.find_overlapping(x+margin, -y+margin, x - margin, -y - margin)

    pixelCollision(mazerunner,pellet1)
    pixelCollision(mazerunner,pellet2)
    pixelCollision(mazerunner,pellet3)
    pixelCollision(mazerunner,pellet4)
    pixelCollision(mazerunner,pellet5)
    pixelCollision(mazerunner,pellet6)
    pixelCollision(mazerunner,pellet7)
    pixelCollision(mazerunner,pellet8)
    pixelCollision(mazerunner,pellet9)
    pixelCollision(mazerunner,pellet10)

    if (len(items) > 0):
        canvas_color = wn_canvas.itemcget(items[0], 'fill')
        if canvas_color == mze_wll_clr:
            mazerunner.color('gray')
            wn.onkeypress(None, 'space')
            return
    wn.ontimer(go_turtle, 15)


#Setup for maze
mazedrawer.pensize(wall_thickness)
mazedrawer.color(mze_wll_clr)
mazedrawer.speed("fastest")

#Drawing the maze


for side in range(num_walls):
    wall_length += path_width
    mazedrawer.color(mze_wll_clr)
    
    if side > 4:
        mazedrawer.left(angle)

        #randomize location of doors and barriers
        door = rand.randint(path_width*2, (wall_length - path_width*2))
        barrier = rand.randint(path_width*2, (wall_length - path_width*2))
        while abs(door - barrier) < path_width:
            door = rand.randint(path_width*2, (wall_length - path_width*2))
        

        if (door < barrier):
            draw_door(door)
            draw_barrier(barrier - door - path_width*2)
            #draw rest of wall  
            mazedrawer.forward(wall_length - barrier)
        else:
            draw_barrier(barrier)
            draw_door(door - barrier)
            #draw rest of wall
            mazedrawer.forward(wall_length - door - path_width*2)    

mazedrawer.hideturtle()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")

wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")

wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")

wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_turtle, "space")

wn.listen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()