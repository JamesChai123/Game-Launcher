from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk, UnidentifiedImageError
from AppOpener import open

root = Tk()
root.title("Application Manager")
root.state('zoomed')

Game_List = []
App_List = []
game_objects = []

class Game:
    def __init__(self, name, image_path=None):
        self.name = name
        self.image_path = image_path
        self.image = self.load_image(image_path)
        self.additional_apps = []

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

            button2 = Button(frame, text="Open Game", command=self.open_all)
            button2.pack(side=TOP)

            game_manager.pos += 1
        if (game_manager.pos % 4) == 0:
            game_manager.y_axis += 1

    def open_all(self):
        open(self.name, match_closest=True)
        for app in self.additional_apps:
            open(app, match_closest=True)

    def game_config(self):
        global config_window
        global config_entry
        config_window = Toplevel(root)
        config_window.geometry("400x400")
        config_window.title("Configuration")
        config_label = tk.Label(config_window, text="Game Configuration")
        config_label.pack()
        config_entry = tk.Entry(config_window)
        config_entry.pack()
        add_btn = tk.Button(config_window, text='Add', command=self.add_app)
        add_btn.pack()
        self.update_app_list()

    def update_app_list(self):
        for widget in config_window.pack_slaves():
            if isinstance(widget, tk.Frame):
                widget.destroy()
        for idx, app in enumerate(self.additional_apps):
            app_frame = tk.Frame(config_window)
            app_frame.pack(fill="x")
            app_label = tk.Label(app_frame, text=app)
            app_label.pack(side="left")
            edit_btn = tk.Button(app_frame, text="Edit", command=lambda idx=idx: self.edit_app(idx))
            edit_btn.pack(side="left")
            del_btn = tk.Button(app_frame, text="Delete", command=lambda idx=idx: self.delete_app(idx))
            del_btn.pack(side="left")

    def add_app(self):
        global config_entry
        app_name = config_entry.get()
        if app_name:
            self.additional_apps.append(app_name)
            config_entry.delete(0, END)
            self.update_app_list()

    def edit_app(self, idx):
        global config_entry
        new_name = config_entry.get()
        if new_name:
            self.additional_apps[idx] = new_name
            config_entry.delete(0, END)
            self.update_app_list()

    def delete_app(self, idx):
        del self.additional_apps[idx]
        self.update_app_list()

class Game_Manager:
    def __init__(self):
        self.entry = None
        self.image_path = None
        self.pos = 0
        self.y_axis = 0

    def submit(self, event=None):
        game_name = self.entry.get()
        image_path = self.image_path
        new_game = Game(game_name, image_path)
        game_objects.append(new_game)
        new_game.add_buttons(root, self)
        inputWindow.destroy()

    def select_image(self):
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if self.image_path:
            self.image_label.config(text=self.image_path)

    def game_input(self):
        global inputWindow
        inputWindow = Toplevel(root)
        inputWindow.geometry("300x150")
        inputWindow.title("Add Application")
        name_label = tk.Label(inputWindow, text="Game Name")
        self.image_label = tk.Label(inputWindow, text="No file selected")
        self.entry = tk.Entry(inputWindow)
        image_btn = tk.Button(inputWindow, text="Select Image", command=self.select_image)
        sub_btn = tk.Button(inputWindow, text='Submit', command=self.submit)
        name_label.pack()
        self.entry.pack()
        image_btn.pack()
        self.image_label.pack()
        sub_btn.pack()
        inputWindow.bind('<Return>', lambda event: self.submit())
        
game_manager = Game_Manager()

add_game_button = tk.Button(root, text="Add Game", command=game_manager.game_input)
add_game_button.pack()

root.mainloop()

