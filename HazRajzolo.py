#haromszog
import turtle

i=0

turtle.left(45)
while i<3:
    turtle.forward(300)
    turtle.right(45)

#hazalja
while i < 4:
    turtle.forward(300)
    turtle.left(-90)

    i+=1

turtle.done()