from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.state('zoomed')

Game_List = []

pos = 0 
y_axis = 0
game_name = ""

class Game_Manager:
    def __init__(self):
        self.entry = None 

    def submit(self):
        global game_name
        game_name = self.entry.get()
        self.add_application()
        inputWindow.destroy()

    def game_input(self):
        global inputWindow
        inputWindow = Toplevel(root)
        inputWindow.title("Add Application")
        name_label = tk.Label(inputWindow, text = "Game Name")
        name_label.pack()
        self.entry = tk.Entry(inputWindow)
        self.entry.pack()
        sub_btn=tk.Button(inputWindow,text = 'Submit', command = self.submit)
        sub_btn.pack()

    def add_application(self):
        global pos
        global y_axis
        global game_name
        Game_List.append(game_name)
        if pos < len(Game_List):
            new_button = Button(root, text=game_name)
            new_button.place(x=125 + (375*(pos%4)),y=150 + (175*(y_axis)))
            pos = pos +1
        if (pos%4) == 0:
            y_axis += 1

add = Button(text="Add Games", command=Game_Manager().game_input)
add.place(x=10, y=10)

root.mainloop()
