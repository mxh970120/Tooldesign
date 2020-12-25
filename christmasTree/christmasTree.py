import turtle

screen = turtle.Screen()
screen.setup(800, 800)

# 隐藏乌龟
turtle.hideturtle()
turtle.speed("fastest")

# 画顶部星星
turtle.penup()
turtle.setposition(-25, 340)
turtle.pencolor("yellow") #画笔黄色
turtle.fillcolor("yellow") #内部填充红色
turtle.begin_fill()
for _ in range(5): #重复执行5次
    turtle.forward(50) #向前移动200步
    turtle.right(144)  #向右移动144度，注意这里的参数一定不能变
turtle.end_fill() #结束填充红色

# 其他
circle = turtle.Turtle()
circle.shape('circle')
circle.shapesize(0.1, 0.1, 0.1)
circle.color('red')
circle.speed('fastest')
circle.up()

circle.goto(0, 280)
circle.stamp()

# 画树
turtle.setposition(0, 100)
turtle.pendown()
n = 75
turtle.left(90)
turtle.forward(3*n)
turtle.color("dark green")
turtle.backward(n*4.8)
def tree(d, s):
    if d <= 0:
        return
    turtle.forward(s)
    tree(d-1, s*.8)
    turtle.right(120)
    tree(d-3, s*.5)
    turtle.right(120)
    tree(d-3, s*.5)
    turtle.right(120)
    circle.goto(turtle.position())
    if d % 4 == 0 or d % 4 == 1:
        circle.color('yellow')
    else:
        circle.color('red')
    circle.stamp()
    turtle.backward(s)

tree(11, n)
turtle.backward(n/2)

# write a festive message
turtle.penup()
turtle.goto(0, -200)
turtle.color("red")
turtle.write("Fröhliche Weihnachten !", True, align="center", font=("Arial", 42, "normal"))


turtle.exitonclick()