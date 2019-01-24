"""Implementation of EPR07 Task 1"""

__author__ = "1234567: Felix Lapp"
__credits__ = "Epr macht Spaß"
__email__ = "felix.lapp@stud.uni-frankfurt.de"
__copyright__ = "by me"

class Presentation:
     """Class representing a presentation"""
     
     def __init__(self, title, date, presenter):
          """Constructor. title and date need to be a string.
          presenter a Member"""
          
          self.title = title
          self.date = date

          # checks if the presenter is a Member
          if not isinstance(presenter, Member):
               raise ValueError("Presenter needs to be instance of Member")
          self.presenter = presenter

          ResearchGroup.total_presentation += 1
          
          print("Presentation", title, "for", date, "created.")
          print("Presenter:", presenter.name)


     def change_date(self, new_date):
          """Replaces the old date by a new one"""
          
          self.date = new_date

class Member:
     """Abstract class. Do not initialize"""
     
     def __init__(self, id, name):
          """id should be a unique integer. Name is string"""
          self.id = id
          self.name = name
          print("Member", name, "with ID", id, "was created")

class WiMi(Member):
     """Subclass of member"""
     def __init__(self, id, name):
          Member.__init__(self, id, name)
          print("WiMi was created")

class Professor(Member):
     """Subclass of member"""

     def __init__(self, id, name, cost_center_no):
          Member.__init__(self, id, name)
          self._cost_center_no = cost_center_no
          print("Professor with cost_center_no", cost_center_no,\
                "was created")

class ResearchGroup:
     """Class representing a ResearchGroup"""

     # total amount of presentations
     total_presentation = 0

     
     def __init__(self, name, members):
          """Constructor. Name needs to be a string.
          members a list of Member-objects."""
          
          self.name = name
          if len(members) == 0:
               raise ValueError("Members list cannot be empty!")

          self.members = members
          # self.head is not needed because it is 0..1

     def get_members(self):
          """Returns a list of members"""
          
          return self.members


     def get_head(self):
          """Returns the head. Can be None"""
          
          return self.head

     # head:Member is enough to tell the type of head
     def set_head(self, head:Member):
          """Sets the head. This needs to be a Member"""
          self.head = head


     def add_member(self, member:Member):
          """Adds a new member to the existing members"""
          self.members.append(member)





if __name__ == "__main__":
     member1 = WiMi(0, "Felix")
     member2 = Professor(1, "Krömker", 9000)
     grp = ResearchGroup("EPR", [member1, member2])
     prs = Presentation("Vorlesung", "24.01.2019", member2)
