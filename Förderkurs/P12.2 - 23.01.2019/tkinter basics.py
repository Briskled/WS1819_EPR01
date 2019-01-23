import tkinter as tk

def print_text(text):
     print(text)

root = tk.Tk()
window = tk.Frame(root)
window.pack()

button = tk.Button(window, text="Text ausgeben", \
                   command=lambda: \
                   print_text("Anderer Text"))
button.pack()

root.mainloop()
