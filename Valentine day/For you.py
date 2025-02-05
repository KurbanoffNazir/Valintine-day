import tkinter as tk
import random


def move_no(event):
    no_button_width = no_button.winfo_width()
    no_button_height = no_button.winfo_height()

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    new_x = random.randint(0, window_width - no_button_width)
    new_y = random.randint(0, window_height - no_button_height)

    no_button.place(x=new_x, y=new_y)


def yes_response():
    result_label.config(text="I didn't doubt u! ❤️")


def no_response():
    result_label.config(text="The answer is not correct. Try again! 😁")


root = tk.Tk()
root.title("Will you be my Valentine?")
root.geometry("400x300")

title_label = tk.Label(root, text="Will you be my Valentine?", font=("Helvetica", 16))
title_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", command=yes_response, width=10)
yes_button.pack(pady=10)

no_button = tk.Button(root, text="No", command=no_response, width=6)
no_button.pack(pady=6)

no_button.bind("<Enter>", move_no)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

root.mainloop()