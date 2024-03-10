import tkinter as tk
from tkinter import messagebox

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200
INSTRUCTION_FOREST = " Find the treasure in the haunted forest.\n Beware of ghosts.\n You can hide behind trees.\n" \
                     "If your level reaches 5, you win 🏆.\n"
INSTRUCTION_OCEAN = "Explore the depths of the ocean to find pearls.\nWatch out for sharks!\n" \
                    "You can hide behind coral reefs.\nReach level 5 to win 🏆."
INSTRUCTION_DESERT = "Navigate through the scorching desert to find ancient treasures.\nBeware of lurking scorpions!\n" \
                     "Rest in hidden oases.\nReach level 5 to win 🏆."

class Instruction():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Select Game Board")
        self.center_window(self.root, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        label = tk.Label(self.frame, text="INSTRUCTION")
        label.pack()

        forest_button = tk.Button(self.frame, text="Forest", command=self.show_instruction_forest)
        forest_button.pack(pady=10)

        ocean_button = tk.Button(self.frame, text="Ocean", command=self.show_instruction_ocean)
        ocean_button.pack(pady=10)

        jungle_button = tk.Button(self.frame, text="Desert", command=self.show_instruction_jungle)
        jungle_button.pack(pady=10)

        self.root.mainloop()

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def show_instruction_forest(self):
        messagebox.showinfo("Forest", INSTRUCTION_FOREST)

    def show_instruction_ocean(self):
        messagebox.showinfo("Ocean", INSTRUCTION_OCEAN)

    def show_instruction_jungle(self):
        messagebox.showinfo("Jungle", INSTRUCTION_DESERT)


