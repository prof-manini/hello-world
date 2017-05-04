"""Commento in locale sul fork"""
def add(a,b):
  """Add two numbers.
  >>> add(2,3)
  5
  """
  return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print(123)
