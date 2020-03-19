import turtle as t
t.setup(900,600)
t.pensize(4)
t.pencolor("black")
for i in range(4):
    t.seth(0)
    t.seth(90 * abs(i - 4))
    t.fd(150)
    t.seth(-90 * (i + 1))
    t.circle(-150, 45)
    t.goto(0, 0)
t.done()