import tkinter as tk

def print_text():
     print("Button wurde gedrückt")

root = tk.Tk()
window = tk.Frame(root)
window.pack()

button = tk.Button(window, text="Text ausgeben", command=print_text)
button.pack()

root.mainloop()
