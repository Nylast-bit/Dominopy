import pygame

class Player: 
  def __init__(self, name, width = 1920, height = 1080):
      self.dominos = []
      self.name = name
      self.width =  0.020 * width
      self.height = 0.070 * height 

  def getDominos(self, Dominos): 
    for _ in range(14):
      self.currentDomino = pygame.image.load("img/" + Dominos[0] + ".gif")
      self.currentDomino = pygame.transform.rotate(self.currentDomino,90)
      self.currentDomino = pygame.transform.scale(self.currentDomino, (self.width, self.height))
      self.dominoRect = self.currentDomino.get_rect()
      self.dominoTanto = (int(Dominos[0][0]) + int(Dominos[0][2]))
      self.dominos.append({
        "name": Dominos[0],
        "valueSurface": self.currentDomino,
        "value": self.dominoRect,
        "tanto": self.dominoTanto
      })
      Dominos.pop(0)


