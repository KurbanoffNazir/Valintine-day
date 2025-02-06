import tkinter as tk
import random

def move_no_button(event):
    # Получаем размеры кнопки "No"
    no_button_width = no_button.winfo_width()
    no_button_height = no_button.winfo_height()

    # Генерируем случайные координаты для кнопки "No"
    new_x = random.randint(0, root.winfo_width() - no_button_width)
    new_y = random.randint(0, root.winfo_height() - no_button_height)

    # Перемещаем кнопку "No"
    no_button.place(x=new_x, y=new_y)

def yes_response():
    response_label.config(text="Yay! I knew you'd agree! ❤️")
    response_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # Подняли текст

def no_response():
    response_label.config(text="It's a lie! Try again! 😁")
    response_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # Подняли текст

# Создаем главное окно
root = tk.Tk()
root.title("Will you be my Valentine?")
root.geometry("400x300")
root.minsize(400, 300)
root.configure(bg="#ffcccb")  # Светло-розовый фон

# Заголовок
title_label = tk.Label(root, text="Will you be my Valentine?", font=("Helvetica", 16), bg="#ffcccb")
title_label.pack(pady=20)

# Кнопка "Yes"
yes_button = tk.Button(root, text="Yes", command=yes_response, bg="#98fb98", activebackground="#98fb98", font=("Helvetica", 12), width=10)
yes_button.pack(side=tk.LEFT, padx=20)

# Кнопка "No"
no_button = tk.Button(root, text="No", command=no_response, bg="#ff7f50", activebackground="#ff7f50", font=("Helvetica", 12), width=10)
no_button.pack(side=tk.RIGHT, padx=20)
            
# Привязываем движение кнопки "No" к движению мыши
no_button.bind("<Enter>", move_no_button)

# Метка для отображения ответа
response_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#ffcccb")
response_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # Центрируем метку ниже заголовка

# Запускаем главный цикл
root.mainloop()
