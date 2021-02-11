from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.color("white")
        self.goto(0, 275)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score()

        self.score = 0
        self.score_board()

    def read_high_score(self):
        with open("data.txt") as f:
            self.high_score = int(f.read())

    def new_high_score(self):
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self .write("GAME OVER", align=ALIGNMENT, font=FONT)
