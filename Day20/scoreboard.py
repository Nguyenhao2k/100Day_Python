from Food import Food
ALIGNMENT = "center"
FONT = ("Lato", 24, "normal")

class scoreboard(Food):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", 'r') as data:
            data = int(data.read())
            self.high_score = data

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Hight Score: {self.high_score}", align = ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0 ,0)
        self.write("GAME OVER", align = ALIGNMENT, font=FONT)
        
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def  reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score() 

        
        
        
    