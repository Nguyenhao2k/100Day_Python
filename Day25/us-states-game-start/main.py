import turtle

import pandas

screen = turtle.Screen()
screen.title("US State Game") 
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_answer = []

while len(guessed_answer) < 50:
    your_answer = screen.textinput(title = f"Guess the State {len(guessed_answer)}/50", prompt = "Enter a state: ").title()


    if your_answer == "Exit":
        # final = pandas.DataFrame(guessed_answer)
        # final.to_csv("Your Answer")
        missing_states = [state for state in states if state not in guessed_answer]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States you need to learn.csv")
        break


        # for state in states:
        #     if state not in guessed_answer:
        #         missing_states.append(state)
            
        


    if your_answer in states: 
        guessed_answer.append(your_answer)
        Check = turtle.Turtle()
        Check.hideturtle()
        Check.penup()
        state_data = data[data.state == your_answer]
        Check.goto(int(state_data.x), int(state_data.y))
        Check.write(your_answer)

screen.exitonclick()



    



# for i in states:
#     if input == states[i]:
#         print("Correct state: ")
#         continue
#     else:
#         print("Invalid state: ")
    

























# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
