from tkinter import *
from tkinter import ttk

root = Tk()
root.state('zoomed')

Game_List = []

pos = 0

def add_application():
    global pos
    Game_List.append("")
    if pos < len(Game_List):
        new_button = Button(root, text="Game {}".format(len(Game_List)))
        new_button.place(x=125 + (375*(pos%4)),y=195)
        pos = pos +1

add = Button(text="Add Games", command=add_application)
add.place(x=10, y=10)

root.mainloop()
