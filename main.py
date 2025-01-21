import turtle
from turtle import Screen,Turtle
import pandas

pen=Turtle()
screen=Screen()
screen.title("Guess the States")
screen.setup(width=735, height=862)
screen.addshape("map.gif")
turtle.shape("map.gif")
pen.penup()
pen.hideturtle()
data=pandas.read_csv("coordinates.csv")
states=data.state.to_list()
guessed=[]
tolearn=[]
'''screen.listen()
def c(x,y):
    print(x,y)
screen.onscreenclick(c)'''

while len(guessed)<28:
    answer=screen.textinput(title=f"{len(guessed)}/28 states guessed",prompt="guess a state:").title()
    if answer in states:
        guessed.append(answer)
        statedata=data[data.state==answer]
        pen.goto(statedata.x.item(),statedata.y.item())
        pen.write(answer)
    if answer.lower()=="exit":
        for i in states:
            if i not in guessed:
                tolearn.append(i)
        break

tolearn=pandas.DataFrame(tolearn)
tolearn.to_csv("states_to_learn")

turtle.mainloop()