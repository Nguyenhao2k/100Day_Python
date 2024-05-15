from tkinter import* 
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONTNAME = "Lora"
WORK_MIN = 25
SORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title = "Password Manager"
window.config(padx = 225, pady = 225, bg = GREEN)
time_Label = Label(text="E", fg=GREEN, bg=YELLOW, font=(FONTNAME, 24, "bold"))
time_Label.grid(column=1, row=0)

canvas = Canvas(width=225, height=225, bg = YELLOW, highlightthickness=0)
PW_img = PhotoImage(file="logo_pw.png")
canvas.create_image(200,200, image=PW_img)
canvas.create_text(113,120, text="00:00", fill="white", font= (FONTNAME, 30, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()