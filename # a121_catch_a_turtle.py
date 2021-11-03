#-----import statements-----
import turtle as trtl
import random as rand
import turtle as trtl2
import turtle as trtl3
import turtle as trtl4
import turtle as trtl5

#-----game configuration----
spot_1 = trtl.Turtle()
score_writer = trtl2.Turtle()
counter = trtl3.Turtle()
ghost = trtl4.Turtle()
spot_2 = trtl5.Turtle()
spot_shape="circle"
spot_color="green"
spot_fillcolor="green"
spot_size=2
spot_speed=0
score=0
score_writer_color="green"
counter_color="red"
start_font=("Arial",100,"normal")
new_xpos=0
new_ypos=0
wn = trtl.Screen()
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 60
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----new spot variable-------
list_color = ["red","blue","green","yellow","white","black"]
list_size = [1,2,3,5]

#-----initialize turtle-----
spot_1.shape(spot_shape)
spot_1.color(spot_color)
spot_1.fillcolor(spot_fillcolor)
spot_1.shapesize(spot_size)
spot_1.speed(spot_speed)
spot_2.shape(spot_shape)
spot_2.color(spot_color)
spot_2.fillcolor(spot_fillcolor)
spot_2.shapesize(spot_size)
spot_2.speed(spot_speed)
score_writer.color(score_writer_color)
counter.color(counter_color)
#Image

#-----game functions--------
def spot_clicked(x,y):
  if (timer_up!=True):
    ghost.goto(spot_1.xcor(),spot_1.ycor())
    ghost.clear()
    update_score()
    if(score==20):
      spot_2.showturtle()
      change_position_2()
    change_position()

  else:
    spot_1.hideturtle()

def spot_clicked_2(x,y):
  if (timer_up!=True):
    ghost.goto(spot_2.xcor(),spot_2.ycor())
    ghost.clear()
    update_score()
    change_position_2()
  else:
    spot_2.hideturtle()

def change_position():
  new_xpos=rand.randint(-400,400)
  new_ypos=rand.randint(-300,300)
  spot_1.penup()
  spot_1.hideturtle()
  spot_1.goto(new_xpos,new_ypos)
  spot_1.pendown()
  spot_1.showturtle()

def change_position_2():
  new_xpos=rand.randint(-400,400)
  new_ypos=rand.randint(-300,300)
  spot_2.penup()
  spot_2.hideturtle()
  spot_2.goto(new_xpos,new_ypos)
  spot_2.pendown()
  spot_2.showturtle()
def update_score():
  global score
  score+=1
  if (score != 1):
    score_writer.clear()
  score_writer.write(score, font=font_setup)
def draw_box():
  spot_1.pendown()
  for t in range(2):
    spot_1.forward(125)
    spot_1.lt(90)
    spot_1.forward(45)
    spot_1.lt(90)

def update_score_2():
  global score
  score-=1
  if (score != 1):
    score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
spot_2.penup()
spot_2.hideturtle()
spot_2.goto(400,400)
spot_1.hideturtle()
spot_1.penup()
spot_1.goto(320,350)
spot_1.penup()
spot_1.goto(175,350)
spot_1.penup()
spot_1.goto(0,0)


score_writer.penup()
score_writer.goto(280,300)

counter.penup()
counter.goto(130,300)
spot_1.showturtle()
counter.hideturtle()
score_writer.hideturtle()

spot_1.onclick(spot_clicked)
spot_2.onclick(spot_clicked_2)




wn.bgcolor("white")
wn.ontimer(countdown, counter_interval)
wn.mainloop()