import turtle


class HalloweenPumpkin:
    def __init__(self):
        self.window = turtle.Screen()
        self.tina = turtle.Turtle()
        self.set_shape("turtle")

    def set_shape(self, shape):
        self.tina.shape(shape)

    def draw_pumpkin(self):
        self.tina.penup()
        self.tina.goto(0, -150)
        self.tina.color("#ff6600")
        self.tina.begin_fill()
        self.tina.circle(150)
        self.tina.end_fill()
        self.tina.left(180)

    def draw_triangle(self, x, y, color):
        self.tina.penup()
        self.tina.goto(x, y)
        self.tina.begin_fill()
        self.tina.color(color)
        self.tina.pendown()
        for _ in range(3):
            self.tina.forward(50)
            self.tina.left(120)
        self.tina.end_fill()

    def draw_square(self, x, y, color):
        self.tina.penup()
        self.tina.goto(x, y)
        self.tina.begin_fill()
        self.tina.color(color)
        self.tina.pendown()
        for _ in range(3):
            self.tina.forward(50)
            self.tina.left(90)
        self.tina.end_fill()

    def draw_teeth(self):
        self.draw_triangle(-35, -20, "#fff")
        self.draw_triangle(0, -20, "#fff")
        self.draw_triangle(35, -20, "#fff")
        self.tina.left(180)

    def draw_eyes(self):
        self.draw_triangle(-70, 50, "#fff")
        self.draw_triangle(0, 50, "#fff")

    def draw_stump(self):
        self.draw_square(-20, 125, "#663300")

    def write_happy_halloween(self):
        self.tina.penup()
        self.tina.goto(-100, -185)
        self.tina.write("Happy halloween!", font=("Arial", 24, "normal"))

    def draw_halloween_pumpkin(self):
        self.draw_pumpkin()
        self.draw_teeth()
        self.draw_eyes()
        self.draw_stump()
        self.write_happy_halloween()
        self.window.exitonclick()