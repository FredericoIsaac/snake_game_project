from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, 275)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self .write("GAME OVER", align=ALIGNMENT, font=FONT)
