a = 6
def foo(bar=1):
     return bar ** 3

def bar(b):
     global a
     if a<b:
          a -= 1
          return foo(b)
     else:
          b = b + 1
          return a + b

for i in range(5):
     print(bar(i), end="+")
