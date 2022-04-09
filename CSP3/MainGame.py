#imports

from turtle import *
from random import choice

from freegames import *

path = Turtle()
writer = Turtle()

aim = vector(5, 0)
pacman = vector(-20, -40)


ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]






font_setup = ("Arial", 20, "normal")

counter =  vector(-360,285)

#countdown_timer
timer = 100
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#Vars
trackerx=-420
trackery=290


state = {'score': 0}
tiles=[
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,
0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,
0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,
0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,
0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,
0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,
2,2,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,2,2,
0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,
0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,
0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,
0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,
0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,
0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,
0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,
0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
]



'''
def countdown():
  counter.color("white")
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    counter.right(5)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
'''


def square(x, y):
    "Draw square using path at (x, y)."
    path.hideturtle()
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()
    
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 19)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

# Add your code here

def world():
    Screen().bgcolor('black')
    path.color('purple')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 19) * 20 - 200
            y = 180 - (index // 19) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')
            if tile == 2:
                path.up()
                path.goto(x + 10, y + 10)
                
    
    update()

def move():
  writer.clear()
  writer.write(state['score'])
  clear()
  
  if valid(pacman + aim):
      pacman.move(aim)
      
  index = offset(pacman)

  if tiles[index] == 1:
      tiles[index] = 2
      state['score'] += 1
      x = (index % 19) * 20 - 200
      y = 180 - (index // 19) * 20
      square(x, y)
        
  up()
  goto(pacman.x + 10, pacman.y + 10)
  dot(20, 'yellow')
  
  for point, course in ghosts:
    if valid(point + course):
        point.move(course)
    else:
      options = [
          vector(5, 0),
          vector(-5, 0),
          vector(0, 5),
          vector(0, -5),
      ]
      plan = choice(options)
      course.x = plan.x
      course.y = plan.y

    up()
    goto(point.x + 10, point.y + 10)
    dot(20, 'red')
    
  update()
  
  for point, course in ghosts:
    if abs(pacman - point) < 19:
        return

  Screen().ontimer(move, 80)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y
    if pacman.x < -170:
        change(270,0)
        print(pacman.x)    
    if pacman.x > 150:
        change(-270,0)
        print(pacman.x)    


Screen().setup(1900, 1000, 500, 400)
Screen().tracer(0, 0)
writer.hideturtle()
writer.goto(370, 160)
writer.color('white')
writer.write(state['score'])
Screen().listen()
hideturtle()
Screen().onkey(lambda: change(5, 0), 'Right')
Screen().onkey(lambda: change(-5, 0), 'Left')
Screen().onkey(lambda: change(0, 5), 'Up')
Screen().onkey(lambda: change(0, -5), 'Down')


world()
move()
done()
