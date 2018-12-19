class Person:

     def __init__(self, gender, name):
          self.__gender = gender
          self.__name = name

     def get_gender(self):
          return self.__gender

     def get_name(self):
          return self.__name



class Student(Person):

     def __init__(self, gender, name, subject):
          Person.__init__(self, gender, name)
          self.subject = subject

     def learn(self):
          print("Student", self.get_name(), "lernt!!")

class Foerderkurs:

     def __init__(self, first_student, tutor):
          self.members = [first_student]
          self.tutor = tutor

     def add_member(self, g):
          self.members.append(g)


p1 = Student("m", "Felix", "Informatik")
p2 = Student("w", "Beyda", "Informatik")
s1 = Student("w", "Anita", "Informatik")
s2 = Student("m", "Fahad", "Informatik")
s3 = Student("w", "Susi", "Kunst")

f = Foerderkurs(s3, p1)
f.add_member(p2)
f.add_member(s1)
f.add_member(s2)
