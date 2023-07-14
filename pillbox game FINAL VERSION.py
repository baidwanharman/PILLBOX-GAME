#PILLBOX GAME BY HARMAN 
# uses physics to simulate a projectile being fired at a target (whose location is randomly generated)

import turtle #we use this library to show the graphics 
import random #allows us to randomize the location 
import math #allows us to do the physics 

player = turtle.Turtle() #intializing turtle
real_player = turtle.Turtle() #setting a turtle for the arcs 
target = turtle.Turtle() #intializing turtle
field = turtle.Turtle() #setting a turtle for the field 

screen = turtle.Screen() #creating a screen for the turtle to draw on 

distance = random.uniform(100.00, 300.00)#setting the distance to the object a random number between 100 and 300 and making sure it is a float
print("the target is %.1f m away" % distance)#printing the distance to the target 


target.hideturtle() #we do not want the little cursor to show 

#designing our starting point 
player.speed(0) #hides the animation 
player.hideturtle() 
player.color("blue") #setting the color to blue 
player.penup()
player.goto(0, 10) #sending the player to the location x: 0, y:10
player.pendown()
#drawing the square for the player 
for i in range(4):
    player.forward(10)
    player.right(90) 

#drawing the field 
field.penup() 
field.goto(0, 0)#setting the location to be the center of the screen 
field.pendown()
field.color("green") #setting the color to green 

#we are setting the len of the field to be double the randomly generated distance  
field_len = distance * 2 
field.forward(field_len)
field.hideturtle() 

#setting location of real player
real_player.penup()
real_player.goto(0, 0) #sending it to the center of the screen 
real_player.pendown()

#drawing pentagon shape of the target 
target.penup()
target.goto(distance, 0) #sending it to the randomly generated distance 
target.pendown()
target.color("red")

#wind resistance

wind = turtle.Turtle()
wind.color("grey")

for i in range(5):
    target.speed(0)
    target.forward(10)
    target.left(72) 

    
hit = False #we set the intial value of hit to be false 
#game loop (will end if a hit is confirmed)
while hit == False:
    
    velocity = float(input("what velocity to use (m/s)?:")) #prompting the user to enter a velocity  (as a float)                  
    angle = float(input("what angle to set (degrees)?:"))   #prompting the user to enter an angle (as a float) 
    distance_x = 0 #set the distance to x at 0
    distance_y = 0 #set the distance to y at 0 

    gravity = -9.806 
    time_step = 0.1 # the simulation will progress 0.1 second at a time 

    x_speed = velocity * math.cos(math.radians(angle)) #the amount which the turtle goes across (the x axes) 
    y_speed = velocity * math.sin(math.radians(angle)) #the amount which the turtle goes up and down (the y axes) 

    #we are using a nested loop for drawing the curves 
    while real_player.ycor() >=0:
        distance_x = distance_x + (x_speed * time_step) #working out the iterations for distance in x 
        distance_y = distance_y + (y_speed * time_step) #working out the iterations for distance in y
        y_speed = y_speed + (gravity * time_step) #calculating the y speed 
        #real_player.speed(0.1)
        real_player.goto(distance_x, distance_y) #draws the trajectory of the curves 
        
    
    missed = distance-distance_x #calculating the distance which the player misses away from the target 

    if abs(distance-distance_x)<=1 and real_player.ycor() <= 0 : #if the target successfully hits the target 
        print("A hit!") #victory statement
        hit=True #value of hit is changed to TRUE so that the loop can end 

    #if the trajectory hits the field, then it prompt the user to try again  
    elif real_player.ycor() <= 0: #if the real player hits the ground
        real_player.penup()
        real_player.goto(0, 0) #resetting the location of the turtle 
        real_player.pendown()
        print("you missed by %.1fm" % missed) #letting the user know how much they missed by 
        print("the target is %.1f m away" % distance)#printing the distance to the target

turtle.done()#letting the program know that we are done 
