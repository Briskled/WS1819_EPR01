import tkinter as tk


class Question:

     def __init__(self, quest, answers, right_index):
          self.quest = quest
          self.answers = answers
          self.right_index = right_index



def main():

     current = 0
     def next_question(current):
          current += 1
          fill_infos(questions[current], question_label, r1, r2, r3)
          return current


     def check_answer(chosen, right, current):
          if chosen == right:
               return next_question(current)
          else:
               quit()
     
     root = tk.Tk()

     frame = tk.Frame(root)
     frame.pack()

     question_label = tk.Label(frame, text="Hier steht die Frage")
     question_label.pack()

     v = tk.IntVar()

     r1 = tk.Radiobutton(frame, text="Antwort 1", variable=v, value=0)
     r1.pack()

     r2 = tk.Radiobutton(frame, text="Antwort 2", variable=v, value=1)
     r2.pack()

     r3 = tk.Radiobutton(frame, text="Antwort 3", variable=v, value=2)
     r3.pack()

     button = tk.Button(frame, text="Bestätigen", command=lambda: check_answer(v.get(), questions[current].right_index, current))
     button.pack()




     q1 = Question("Wie viele Tage hat eine Woche", ["7 Tage", "42 Tage", "1337 Tage"], 0)
     q2 = Question("Was ist die Antwort auf alles?", ["Weiß nicht", "42", "DANN GEH DOCH ZU NETTO"], 1)


     questions = [q1, q2]
     
     fill_infos(q1, question_label, r1, r2, r3)

     root.mainloop()


def fill_infos(question, label, r1, r2, r3):
     label["text"] = question.quest
     r1["text"] = question.answers[0]
     r2["text"] = question.answers[1]
     r3["text"] = question.answers[2]


if __name__ == "__main__":
     main()
