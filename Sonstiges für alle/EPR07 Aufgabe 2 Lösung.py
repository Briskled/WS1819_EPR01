"""Working Heap-Sort"""

__author__ = "1234567: Felix Lapp"
__credits__ = "Epr macht Spaß"
__email__ = "felix.lapp@stud.uni-frankfurt.de"
__copyright__ = "by me"

# MISTAKE 1: from math import * is wrong and not needed
#              same thing for import random


class SortTree:
     # MISTAKE 2: Docstring missing
     """Heap-tree for sorting a list using heap-sort"""

     # MISTAKE 3: There needs to be a blank between # and the first letter
     # constructor

     # MISTAKE 4: __ was missing
     def __init__(self, unsorted_list):
          # MISTAKE 5: Docstring missing
          
          """Constructor of SortTree. unsorted_list needs to be a list"""
          self.list = unsorted_list

     
     # MISTAKE 6: There needs to be a blank between # and the first letter
     # exchange operation

     # MISTAKE 7: Do not use CamelCase
     def exchange_node(self, i, j):
          # MISTAKE 8: Docstring was missing
          """This swaps two nodes at the given indexes i and j"""

          # MISTAKE 9: Swap i and j
          self.list[i], self.list[j] = self.list[j], self.list[i]

     # MISTAKE 10: Comments in english!
     # iterativ by Robert Sedgewick

     # MISTAKE 11: Do not use CamelCase
     def sink_node(self, index):
          # MISTAKE 12: Docstring was missing
          """repairs the heap down by starting at the given index"""
          
          max_index = len(self.list)
          k = index + 1 #well, i and j are reserved for comparing later

          # MISTAKE 13: The : was missing
          while 2 * k <= max_index:
               j = 2 * k

               # MISTAKE 14: Logic mistake. j > max_index should be j < max_index
               if j < max_index and self.list[j - 1] < self.list[j]:
                    # if left child < right child
                    # then only the right child is valid for exchanging
                    j += 1


               # MISTAKE 15: Brackets are not needed
               if self.list[k - 1] >= self.list[j - 1]:
                    break
               self.exchange_node(k - 1, j - 1)
               k=j

               
     def get_highest_node(self):
          # MISTAKE 16: Missing docstring
          """Returns and removes the highest node. Repairs the heap"""
          a = self.list[0]

          # MISTAKE 17: , instead of ;
          self.exchange_node(0, -1)
          del self.list[-1]
          self.sink_node(0)

          # MISTAKE 18: Variable a should be returned. Not "a"
          return a

# MISTAKE 19: Main-Funktion was missing
def main():
     
     # MISTAKE 20: unsorted out of class 
     unsorted = [2992, 6776, 8185, 8537, 9369, 5980, 8941, 2930, 7567, 1454,\
               2932, 5568, 2599, 3127, 4101, 3621, 6252, 2369, 6410, 4259,\
               3759, 1811, 4820, 5861, 5526, 4224, 7607, 7537, 1796, 193]
     #MISTAKE 21: ] instead of )


     ########### ADDITION FOR CONSOLE INPUT ###########
     # I felt free to not work around every possible wrong input.

     choice = None
     while choice != "Y" and choice != "N":
          choice = input("Do you want to use the default unsorted list? (Y/N) >>> ")

     if choice == "N":
          unsorted = eval(input("Please give a new list in python-syntax. e.g. [5,1,2] >>> "))

     ###################################################



     #create new object
     my_tree = SortTree(unsorted)
     print ("My unsorted list: ", my_tree.list)

     #build a heap, let sink new nodes
     for i in range(len(my_tree.list) - 1, -1, -1):
          my_tree.sink_node(i)

     # create the new sorted list
     output = [my_tree.get_highest_node() for i in range(len(my_tree.list))]
     output.reverse() #yes, that’s right so

     # MISTAKE 22: Cannot add String and list
     print ("\nMy sorted list: ", output)


if __name__ == "__main__":
     main()
