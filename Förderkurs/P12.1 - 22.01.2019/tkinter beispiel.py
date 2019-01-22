import tkinter as tk

def print_cool_stuff():
     print("Käsekuchen")


root = tk.Tk()
f = tk.Frame(root)
f.pack()

button1 = tk.Button(f, text="Beenden", fg="red", command=print_cool_stuff)
button1.pack(side=tk.LEFT)

root.mainloop()
