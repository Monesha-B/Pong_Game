from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.shapesize(stretch_len=0.75, stretch_wid=5)
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.goto(x_axis, y_axis)

    def paddle_up(self):
        # self.goto(350, 250)
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        # self.goto(350, -250)
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)