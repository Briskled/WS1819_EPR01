import tkinter as tk

# an den Anfang
root = tk.Tk()


def print_it(text):
     print(text)



frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(frame, text="Print it!", command=lambda: print_it(entry.get()))
button.pack()



# ans ende!
root.mainloop()
