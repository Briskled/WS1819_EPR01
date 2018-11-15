"""Docstring: Creates a list with all possible classes.

"""

__author__ = "1234567: Felix Lapp"
__credits__ = "luv u xoxo"
__email__ = "felix.lapp@stud.uni-frankfurt.de"

def main():
     """Docsting: Main-function
     """
     print("Ist main")
     years = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
     classes = ["a", "b", "c", "d", "e", "f"]

     combinations = []
     # create all combinations out of years and classes:
     for x in years:
          for y in classes:
               school_class = (x, y)
               combinations.append(school_class)


# googlen:     pop
#              shuffle

if __name__ == "__main__":
     main()

















