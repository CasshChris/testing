import turtle
print("draw flower")
t = turtle.Turtle()
t.shape("turtle")
t.color('red','yellow')
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) <1:
        break
t.end_full()
turtle.dome()
