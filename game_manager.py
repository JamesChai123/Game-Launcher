from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from AppOpener import open

root = Tk()
root.title("Application Manager")
root.state('zoomed')

Game_List = []

pos = 0 
y_axis = 0
game_name = ""
path = ""

class Game_Manager:
    def __init__(self):
        self.entry = None 

    def submit(self, event=None):
        global game_name
        global game_path
        global game_image
        game_name = self.entry.get()
        path = self.image_entry.get()
        game_path = path.replace('"','')
        image = Image.open(game_path)
        resize_image = image.resize((50, 50))
        game_image = ImageTk.PhotoImage(resize_image)
        self.add_application()
        inputWindow.destroy()

    def game_input(self):
        global inputWindow
        inputWindow = Toplevel(root)
        inputWindow.geometry("150x150")
        inputWindow.title("Add Application")
        name_label = tk.Label(inputWindow, text="Game Name")
        image_label = tk.Label(inputWindow, text="PNG Image Path")
        self.entry = tk.Entry(inputWindow)
        self.image_entry = tk.Entry(inputWindow)
        sub_btn = tk.Button(inputWindow, text='Submit', command=self.submit)
        name_label.pack()
        self.entry.pack()
        image_label.pack()
        self.image_entry.pack()
        sub_btn.pack()
        inputWindow.bind('<Return>', lambda event: self.submit())

    def open_game(self, game_name):
        open(game_name, match_closest=True)
                
    def add_application(self):
        global pos
        global y_axis
        global new_button
        Game_List.append(game_name)
        if pos < len(Game_List):
            new_button = Button(root, text=game_name, image=game_image, compound="top", command=lambda name=game_name: self.open_game(name))
            new_button.image = game_image
            new_button.place(x=125 + (375 * (pos % 4)), y=150 + (175 * (y_axis)))
            pos = pos + 1
        if (pos % 4) == 0:
            y_axis += 1
    
add = Button(text="Add Games", command=Game_Manager().game_input)
add.place(x=10, y=10)

root.mainloop()