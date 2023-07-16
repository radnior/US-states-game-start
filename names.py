import turtle

class Names(turtle.Turtle):
    def __init__(self, x,y, answer):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.hideturtle()
        self.write(answer)