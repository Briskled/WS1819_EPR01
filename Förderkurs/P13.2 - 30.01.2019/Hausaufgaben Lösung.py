"""A simple dictionary user interface"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


# dictionary which contains some words and their english translations
dictionary = {"Hund" : "Dog",
              "Fliege" : "Fly",
              "Tisch" : "Table",
              "Stuhl" : "Chair"}

def search(word):
     """Searches the given word in the dictionary and shows the translation
     If the word is not found it will try a backword search"""
     
     if word in dictionary:
          tk.messagebox.showinfo("Treffer!", \
                                 "Die englische Übersetzung von "+word+": "+dictionary[word])
     else:
          backword_search(word)

def backword_search(word):
     """Searches all given translations and shows the german word
     Shows an error if there is no such word"""

     # iterate over all keys in the dictionary
     for key in dictionary:

          # if the value to that key is the given word
          # it will show the key (which is the german word)
          if dictionary[key] == word:
               tk.messagebox.showinfo("Treffer!", \
                                      "Die deutsche Übersetzung von "+word+\
                                      ": "+key)

               # in that case: Break everything up
               return

     # if this is reached it means that there is no german word for the given english word
     # because in that case the function would have been breaked up
     tk.messagebox.showerror("Error", "Dieses Wort ist uns nicht bekannt")


def append_to_dictionary(g, e):
     dictionary[g] = e

def save_dictionary():
     file_name = filedialog.asksaveasfilename(title="Choose a file to save the dictionary")
     
     file = open(file_name, "x")
     file.write(str(dictionary))
     file.close()


def load_dictionary(dictionary):
     file_name = filedialog.askopenfilename(title="Choose a dictionary",
                                           filetypes=(   ("Textdateien", "*.txt"),\
                                                         ("Python", "*.py")   ))
     print(file_name)
     file = open(file_name, "r")
     loaded_dictionary = eval(file.read())
     file.close()
          
     dictionary.clear()

     for key in loaded_dictionary:
          value = loaded_dictionary[key]
          dictionary[key] = value
     


def main():
     root = tk.Tk()

     # new window
     frame = tk.Frame(root)
     frame.pack()

     # put a textfield on it
     word_input = tk.Entry(frame)
     word_input.pack()

     # put a button on it
     search_button = tk.Button(frame, text="Übersetzen", \
                               command=lambda: search(word_input.get()))
                              # reads the word from the textfield. This should be the word
                              # we are searching for.
     search_button.pack()

     german_word = tk.Entry(frame)
     german_word.pack()

     english_word = tk.Entry(frame)
     english_word.pack()

     button2 = tk.Button(frame, text="Einfügen", \
                         command = lambda: append_to_dictionary(\
                              german_word.get(), english_word.get()))
     button2.pack()

     save_button = tk.Button(frame, text="Speichern", command=save_dictionary)
     save_button.pack()

     load_button = tk.Button(frame, text="Laden", command=lambda: load_dictionary(dictionary))
     load_button.pack()

     root.mainloop()

if __name__ == "__main__":
     main()
