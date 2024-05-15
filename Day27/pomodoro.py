from itertools import count
from multiprocessing.resource_sharer import stop
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONTNAME = "Lora"
WORK_MIN = 25
SORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


#---------------------------------------------TIMER SET----------------------------------------------------------------#


#---------------------------------------------TIMER MECHANISM----------------------------------------------------------#


#---------------------------------------------COUNTDOWN MECHANISM -----------------------------------------------------#
import time

while True:
    time.sleep(1)
    count -= 1
    

#---------------------------------------------UI SET UP ---------------------------------------------------------------#

window =Tk()
window.title = "POMODORO"
window.config(padx = 100, pady = 50, bg = YELLOW)
time_Label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONTNAME, 30, "bold"))
time_Label.grid(column=1, row=0)

canvas = Canvas(width=225, height=225, bg = YELLOW, highlightthickness=0)
Tomato_img = PhotoImage(file="tomato_img.png")
canvas.create_image(113,113, image=Tomato_img)
canvas.create_text(113,120, text="00:00", fill="white", font= (FONTNAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_Button = Button(text="Start", highlightthickness=0)
start_Button.grid(column=0, row =2)
stop_Button = Button(text="Stop", highlightthickness=0)
stop_Button.grid(column=2, row =2)

check_Marker = Button(text="✔", fg=GREEN, bg=YELLOW)
check_Marker.grid(column=1, row =3)








window.mainloop()