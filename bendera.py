import turtle

bendera = turtle.Turtle()


# Batang Kayu Coklat
bendera.color("brown")

bendera.begin_fill()
bendera.forward(10)
bendera.left(90)
bendera.forward(300)
bendera.left(90)
bendera.forward(10)
bendera.left(90)
bendera.forward(300)
bendera.end_fill()

bendera.penup()
bendera.left(90)
bendera.forward(10)
bendera.left(90)
bendera.forward(300)
bendera.pendown()


# Bendera
bendera.color("black", "red")

bendera.begin_fill()
bendera.right(90)
bendera.forward(200)
bendera.right(90)
bendera.forward(50)
bendera.right(90)
bendera.forward(200)
bendera.end_fill()

bendera.color("black", "white")

bendera.begin_fill()
bendera.left(90)
bendera.forward(50)
bendera.left(90)
bendera.forward(200)
bendera.left(90)
bendera.forward(50)
bendera.left(90)
bendera.forward(200)
bendera.end_fill()


turtle.done()