#space invader 1 enemy

import turtle
import os
import math

#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state, ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it need change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"

    #move the bullet to the just above player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()

def iscollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15 :
        return True
    else:
        return False



#create keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet,"space")

#main game loop
while True:

    #move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    
    #move the bullet
    if bulletstate =="fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    
    #check for a collision betww the bullet and the enemy
    if iscollision(bullet, enemy):
        #reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"     
        bullet.setposition(0, -400)
        #reset enemy
        enemy.setposition(-200, 250)

    if iscollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break





wn.mainloop()