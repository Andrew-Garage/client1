import tkinter as tk
from tkinter import ttk

def update_label(value):
    int_value = round(float(value))  # Преобразуем значение в целое число
    label.config(text=str(int_value))  # Обновляем текст метки при изменении значения шкалы

root = tk.Tk()
root.minsize(200, 70)
root.title("Laboratory")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

horizontalScale_frame = tk.Frame(root)
horizontalScale_frame.pack(pady=10)

horizontalScale = ttk.Scale(horizontalScale_frame, orient=tk.HORIZONTAL, length=200, from_=0, to=255, value=0, command=update_label)
horizontalScale.pack(side=tk.LEFT, padx=10, pady=30)

label = ttk.Label(horizontalScale_frame, text="0")
label.pack(side=tk.LEFT, padx=30, pady=10)

button_frame = tk.Frame(root)  # Контейнер для кнопок
button_frame.pack(pady=10)

b1 = ttk.Button(button_frame, text="Button 1")
b1.pack(side=tk.LEFT, padx=10, pady=10)

b2 = ttk.Button(button_frame, text="Button 2")
b2.pack(side=tk.LEFT, padx=10, pady=10)

b3 = ttk.Button(button_frame, text="Button 3")
b3.pack(side=tk.LEFT, padx=10, pady=10)

b4 = ttk.Button(button_frame, text="Button 4")
b4.pack(side=tk.LEFT, padx=10, pady=10)

label2_frame = tk.Frame(root)  # Контейнер для пометки перед label2
label2_frame.pack(pady=10)

label2_marker = ttk.Label(label2_frame, text="Энкодер:")
label2_marker.pack(side=tk.LEFT)

label2 = ttk.Label(label2_frame, text="0")
label2.pack(side=tk.LEFT, padx=30, pady=30)

root.mainloop()

