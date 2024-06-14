import tkinter as tk
from tkinter import PhotoImage
import subprocess

class BaseGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Choose a Game")
        self.root.config(padx=20, pady=20, bg="#375362")

        # Descriptive label
        self.label = tk.Label(self.root, text="Select a game to play:", fg="white", bg="#375362", font=("Arial", 18, "bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Load images
        self.image1 = PhotoImage(file="images/pong.png")
        self.image2 = PhotoImage(file="images/snake.png")
        self.image3 = PhotoImage(file="images/quiz.png")
        self.image4 = PhotoImage(file="images/turtle.png")

        # Create buttons with images and associated scripts
        self.create_image_button(self.image1, 1, 0, "Play Pong", PongGame)
        self.create_image_button(self.image2, 1, 1, "Play Snake", SnakeGame)
        self.create_image_button(self.image3, 2, 0, "Take a Quiz", QuizGame)
        self.create_image_button(self.image4, 2, 1, "Play Turtle Graphics", TurtleGame)

    def create_image_button(self, image, row, column, tooltip_text, game_class):
        button = tk.Button(self.root, image=image, command=lambda: self.on_image_click(game_class), bd=0, bg="#375362", activebackground="#375362")
        button.grid(row=row, column=column, padx=20, pady=20)
        create_tooltip(button, tooltip_text)

    def on_image_click(self, game_class):
        self.root.withdraw()  # Hide the main window
        game_instance = game_class()
        game_instance.run()
        self.root.deiconify()  # Show the main window again

class PongGame:
    def run(self):
        subprocess.run(["python", "pong/pong_main.py"])

class SnakeGame:
    def run(self):
        subprocess.run(["python", "snake/snake_main.py"])

class QuizGame:
    def run(self):
        subprocess.run(["python", "quiz/quiz_main.py"])

class TurtleGame:
    def run(self):
        subprocess.run(["python", "turtle/turtle_main.py"])

def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget, bg="white", padx=5, pady=5)
    tooltip.overrideredirect(True)
    tooltip.withdraw()
    tk.Label(tooltip, text=text, bg="white", fg="black", font=("Arial", 10, "italic")).pack()

    def show_tooltip(event):
        tooltip.geometry(f"+{event.x_root+10}+{event.y_root+10}")
        tooltip.deiconify()

    def hide_tooltip(event):
        tooltip.withdraw()

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

if __name__ == "__main__":
    root = tk.Tk()
    app = BaseGameApp(root)
    root.mainloop()
