from random import shuffle


class Dominos:
  def __init__(self):
    self.dominos = []

  def generate(self):
    for left in range(0,7):
      for right in range(0,7):
        current_domino = str(left) +"-"+str(right)
        if not current_domino[::-1] in self.dominos:
          self.dominos.append(current_domino)
  
  def shuffle(self):
    shuffle(self.dominos)
