import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.backward(size/1.732)
    t.left(30)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

order = input("Please enter number of recursions >>> ")
try:
    order = int(order.strip())
    if(order <= 0):
        raise ValueError
except:
    print('Something went wrong. Please enter number more than 0!')
    order = 3
    print('By default drawn for 3!')

draw_koch_curve(order)