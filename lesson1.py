from turtle import *

#background
import turtle
tur=turtle.Screen()
tur.bgcolor("lightblue")



# base
speed(10)
width(4)
color("lightblue")

right(90)
forward(200)

color("dimgray")
begin_fill()

right(90)
forward(100)

right(90)
forward(200)

right(90)
forward(200)

right(90)
forward(200)

right(90)
forward(100)

end_fill()

penup()
goto(100, 0)
pendown()

color("black")
left(90)
forward(200)

right(90)
forward(200)

right(90)
forward(200)

right(90)
forward(200)
#end of base


#door
penup()
goto(0, -200)
pendown()

color("khaki")
begin_fill()

forward(30)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)
left(90)
forward(30)

end_fill()

width(4)

penup()
goto(0, -200)
pendown()

color("black")
forward(30)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)
left(90)
forward(30)
left(90)
forward(80)
#end door


#top
penup()
goto(100, 0)
pendown()

color("firebrick")
begin_fill()
left(50)
forward(130)

left(80)
forward(130)

end_fill()
#end top


#window1
penup()
goto( 40, -40)
pendown()

color("slategray")
begin_fill()
left(50)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto( 40, -40)
pendown()

color("black")
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

#window2
penup()
goto( -40, -40)
pendown()

color("slategray")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

end_fill()

penup()
goto( -40, -40)
pendown()

color("black")

right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
#end windows


#again top
penup()
goto(100, 0)
pendown()

color("black")

left(140)
forward(130)

left(80)
forward(130)

exitonclick()

#end code

#მოხარული ვიქნები თუ თქვენთან სწავლის საშუალება მომეცემა
#ირაკლი გ.