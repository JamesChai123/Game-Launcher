from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk, UnidentifiedImageError
from AppOpener import open

root = Tk()
root.title("Application Manager")
root.state('zoomed')

Game_List = []
game_objects = []

class Game:
    def __init__(self, name, image_path=None):
        self.name = name
        self.image_path = image_path
        self.image = self.load_image(image_path)

    def load_image(self, image_path):
        try:
            if image_path:
                image = Image.open(image_path)
                resize_image = image.resize((50, 50))
                return ImageTk.PhotoImage(resize_image)
            else:
                return None
        except (FileNotFoundError, UnidentifiedImageError):
            return None

    def add_buttons(self, root, game_manager):
        Game_List.append(self.name)
        if game_manager.pos < len(Game_List):
            frame = Frame(root)
            frame.place(x=125 + (375 * (game_manager.pos % 4)), y=150 + (175 * game_manager.y_axis))

            button1 = Button(frame, text=self.name, compound="top", command=self.game_config)
            if self.image:
                button1.config(image=self.image)
                button1.image = self.image
            button1.pack(side=TOP)

            button2 = Button(frame, text="Open Game", command=lambda name=self.name: open(name))
            button2.pack(side=TOP)

            game_manager.pos += 1
        if (game_manager.pos % 4) == 0:
            game_manager.y_axis += 1

    def game_config(self):
        global config_window
        config_window = Toplevel(root)
        config_window.geometry("400x400")
        config_window.title(self.name,"configuration")
        config_label = tk.Label(config_window, text = "Game Configuration")
        


class Game_Manager:
    def __init__(self):
        self.entry = None
        self.image_entry = None
        self.pos = 0
        self.y_axis = 0

    def submit(self, event=None):
        game_name = self.entry.get()
        image_path = self.image_entry.get().replace('"', '')
        new_game = Game(game_name, image_path)
        game_objects.append(new_game)
        new_game.add_buttons(root, self)
        inputWindow.destroy()

    def game_input(self):
        global inputWindow
        inputWindow = Toplevel(root)
        inputWindow.geometry("300x150")
        inputWindow.title("Add Application")
        name_label = tk.Label(inputWindow, text="Game Name")
        image_label = tk.Label(inputWindow, text="PNG Image Path (Optional)")
        self.entry = tk.Entry(inputWindow)
        self.image_entry = tk.Entry(inputWindow)
        sub_btn = tk.Button(inputWindow, text='Submit', command=self.submit)
        name_label.pack()
        self.entry.pack()
        image_label.pack()
        self.image_entry.pack()
        sub_btn.pack()
        inputWindow.bind('<Return>', lambda event: self.submit())

game_manager = Game_Manager()

add_game_button = tk.Button(root, text="Add Game", command=game_manager.game_input)
add_game_button.pack()

root.mainloop()
