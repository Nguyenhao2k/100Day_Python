from tkinter import*

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Nguyenroses")
window.config(padx = 50, pady = 50, background = BACKGROUND_COLOR)

canvas = Canvas(width = 800, height = 526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image = card_front_image)
canvas.grid(row = 1, column = 0)


window.mainloop()

