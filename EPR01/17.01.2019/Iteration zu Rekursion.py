def iter(n):
     sum = 0
     for i in range(n):
          sum += 2*i + 1
     return sum


def rek(i):
     if i == 0:
          return 0
     return 2*(i-1) + 1 + rek(i-1)
