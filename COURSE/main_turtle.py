import turtle

def stairs(size, angle, number):

    for i in range(0, number):
        t.forward(size)
        t.left(angle)
        t.forward(size)
        t.right(angle)
        size -= 10
    t.forward(size)

def square(size, angle, number):
    for i in range(0, number):
        t.forward(size)
        t.left(angle)

def squares(beginning_size, number):
    #10 / 20 / 30 / 40
    for i in range(0, number):
        size = (i+1)*beginning_size
        square(size, 90, 4)
        t.left(4)




t = turtle.Turtle()

#stairs(30, 90, 10)
#square(100, 90, 4)
#square(50, 90, 4)
squares(10, 10)

turtle.done()



#
