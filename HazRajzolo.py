import turtle

turtle.color("red")
turtle.pensize(5)
turtle.speed(0)
t = turtle.Turtle()

#negyzet
i=0
while i < 4:
    turtle.forward(200)
    turtle.left(-90)
    i+=1

#hazteteje
t.pensize(5)
t.color("red")
t.setheading(60)
t.forward(200)
t.setheading(-60)
t.forward(200)


turtle.done()