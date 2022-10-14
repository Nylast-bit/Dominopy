import sys, pygame
from dominos import Dominos
from player import Player
import time

class Game:
  def __init__(self): 
    pygame.init()
   
   #Variables
    self.display = pygame.display.Info()
    self.size = self.width, self.height = self.display.current_w, self.display.current_h
    self.bg = 255,255,255
    self.screen = pygame.display.set_mode(self.size)
    self.player = Player("juan", self.width, self.height)
    self.machine = Player("Bot", self.width, self.height)
    self.bg_img = pygame.image.load("img/Background.jpg").convert()
    self.pass_btn = pygame.image.load("img/next.png")
    self.pass_btn_rect = self.pass_btn.get_rect()
    self.font = pygame.font.Font("fonts/Oswald-VariableFont_wght.ttf", 32)
    self.textPass = self.font.render("Pasar", True, (255,255,255))
    self.textRect = self.textPass.get_rect()
    self.pass_btn_rect.x, self.pass_btn_rect.y = self.width - 120, self.height - 130

    self.textRect.x, self.textRect.y =  self.width - 120, self.pass_btn_rect.y + 55
    self.bg_img = pygame.transform.scale(self.bg_img, (1850, 900))
    self.screen.blit(self.bg_img, (0,0))
    self.screen.blit(self.pass_btn, self.pass_btn_rect)
    self.screen.blit(self.textPass, self.textRect)
    self.board = []
    self.directionHead = "up"
    self.directionTail = "down"
    self.arrow_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
    self.hand_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
    self.direction_play = 'up'
    self.play_up = pygame.image.load("img/down.png")
    self.play_up_rect = self.play_up.get_rect()
    self.play_up_rect.x, self.play_up_rect.y = self.width / 4 , self.height - 100
    self.reset = pygame.image.load("img/restart.png")
    self.resetRect = self.reset.get_rect()
    self.resetRect.x, self.resetRect.y = self.width - 80, 20
    self.exit = pygame.image.load("img/exit.png")
    self.exitRect = self.reset.get_rect()
    self.exitRect.x, self.exitRect.y = self.width - 40, 20
    self.play_down = pygame.image.load("img/up.png")
    self.play_down_rect = self.play_down.get_rect()
    self.play_down_rect.x, self.play_down_rect.y = self.width / 1.5 , self.height - 100
    self.screen.blit(self.play_up, self.play_up_rect)
    self.screen.blit(self.play_down, self.play_down_rect)
    self.screen.blit(self.reset, self.resetRect)
    self.screen.blit(self.exit, self.exitRect)
    self.plus = 1
    self.plusT = 1
    self.plusF = 1
    self.turn = 1
    self.clock =  pygame.time.Clock()


  def printRestartAndExit(self):
      self.screen.blit(self.exit, self.exitRect)
      self.screen.blit(self.reset, self.resetRect)

  def win(self):
    self.confirm = []
    self.sejugo = False
    self.finish = False 
    
    if len(self.player.dominos) == 0 and len(self.machine.dominos) > 0:
      self.screen.blit(self.bg_img, (0,0))
      self.resultText = self.font.render("has ganado!!!", True, (255,255,255))
      self.resultTextRect = self.resultText.get_rect()
      self.resultTextRect.x, self.resultTextRect.y =  self.width / 2 - (self.resultTextRect.width / 2), self.height / 2 - (self.resultTextRect.height/2)
      self.screen.blit(self.resultText, self.resultTextRect)
      self.hand()
      self.handbot()
      self.finish = True
      self.printRestartAndExit()
      return 


    elif len(self.machine.dominos) == 0 and len(self.player.dominos) > 0:
      self.screen.blit(self.bg_img, (0,0))
      self.resultText = self.font.render("Has perdido, y nada más pone ficha!!!", True, (255,255,255))
      self.resultTextRect = self.resultText.get_rect()
      self.resultTextRect.x, self.resultTextRect.y =  self.width / 2 - (self.resultTextRect.width / 2), self.height / 2 - (self.resultTextRect.height/2)
      self.screen.blit(self.resultText, self.resultTextRect)
      self.finish = True
      self.hand()
      self.handbot()
      self.printRestartAndExit()
      return 

    if len(self.head["name"]) > 0:
      for index in range(len(self.player.dominos)): 
        if (self.player.dominos[index-1]["name"][0] == self.head["name"] or 
          self.player.dominos[index-1]["name"][2] == self.head["name"]):
          self.sejugo = True
          break

        elif (self.player.dominos[index-1]["name"][0] == self.tail["name"] or 
          self.player.dominos[index-1]["name"][2] == self.tail["name"]):
          self.sejugo = True
          break

      
      if not self.sejugo:
        self.confirm.append(self.player)

      self.sejugo = False

      for index in range(len(self.machine.dominos)): 
        if (self.machine.dominos[index-1]["name"][0] == self.head["name"] or 
          self.machine.dominos[index-1]["name"][2] == self.head["name"]):
          self.sejugo = True
          break

        elif (self.machine.dominos[index-1]["name"][0] == self.tail["name"] or 
          self.machine.dominos[index-1]["name"][2] == self.tail["name"]):
          self.sejugo = True
          break

      if not self.sejugo:
        self.confirm.append(self.machine)

    if len(self.confirm) == 2:
      self.tantosPlayer = 0
      self.tantosMachine = 0

      for currentDomino in self.player.dominos: 
        self.tantosPlayer += currentDomino["tanto"]

      for currentDomino in self.machine.dominos: 
        self.tantosMachine += currentDomino["tanto"]

      if self.tantosPlayer < self.tantosMachine:
        self.screen.blit(self.bg_img, (0,0))
        self.resultText = self.font.render("Se trancó, has ganado!!!", True, (255,255,255))
        self.resultTextRect = self.resultText.get_rect()
        self.resultTextRect.x, self.resultTextRect.y =  self.width / 2 - (self.resultTextRect.width / 2), self.height / 2 - (self.resultTextRect.height/2)
        self.screen.blit(self.resultText, self.resultTextRect)
        self.hand()
        self.handbot()
        self.finish = True 
        self.printRestartAndExit()
        return 
      else: 
        self.screen.blit(self.bg_img, (0,0))
        self.resultText = self.font.render("Se trancó, has perdido y nada más tira fichas!!!", True, (255,255,255))
        self.resultTextRect = self.resultText.get_rect()
        self.resultTextRect.x, self.resultTextRect.y =  self.width / 2 - (self.resultTextRect.width / 2), self.height / 2 - (self.resultTextRect.height/2)
        self.screen.blit(self.resultText, self.resultTextRect)
        self.hand()
        self.handbot()
        self.finish = True
        self.printRestartAndExit()
        return
        


  def hand(self):
    self.placeX = self.width / 3
    for domino in self.player.dominos: 
      domino["value"].x,domino["value"].y  = self.placeX, self.height - 100
      self.screen.blit(domino["valueSurface"] , domino["value"])
      self.placeX += self.player.width + 2

  def handbot(self):
    self.placeX = 530
    for domino in self.machine.dominos: 
      domino["value"].x,domino["value"].y  = self.placeX, 150
      self.screen.blit(domino["valueSurface"] , domino["value"])
      self.placeX += self.player.width

  def refreshGame(self):
    self.screen.blit(self.bg_img, (0,0))
    self.screen.blit(self.pass_btn, self.pass_btn_rect)
    self.screen.blit(self.textPass, self.textRect)
    self.screen.blit(self.reset, self.resetRect)
    self.screen.blit(self.exit, self.exitRect)
    if(self.direction_play == 'up' and self.turn == 1):
      self.screen.blit(self.play_down, self.play_down_rect)
    elif(self.direction_play == 'down'and self.turn == 1):
      self.screen.blit(self.play_up, self.play_up_rect)
    
    
    for domino in self.board: 
      self.screen.blit(domino["valueSurface"] , domino["value"])
    if self.turn == 1: 
      self.hand()

    

  def outputDoubleSix(self, player):
    for index in range(len(player.dominos)): 
      if self.doubleSix == player.dominos[index-1]["name"]:
        player.dominos[index-1]["value"].x = self.width/2 - self.player.width
        player.dominos[index-1]["value"].y = self.height/2 - self.player.height
        player.dominos[index-1]["valueSurface"] = pygame.transform.rotate(player.dominos[index-1]["valueSurface"], 90)
        self.screen.blit(player.dominos[index-1]["valueSurface"] , player.dominos[index-1]["value"])
        self.head = {
          "name": player.dominos[index-1]["name"][2],
          "domino": player.dominos[index-1]
        }
        self.tail = {
          "name": player.dominos[index-1]["name"][0],
          "domino":player.dominos[index-1]
        } 
        self.board.append(player.dominos[index-1])
        player.dominos.pop(index-1)


  def calculateTurnGame(self):
    if len(self.head["name"]) > 0:
      if self.head["domino"]["value"].y + self.player.width <= 75 and self.directionHead == 'up':
        self.directionHead = 'left'
      elif self.head["domino"]["value"].x < 75 and self.directionHead == 'left':
        self.directionHead = 'down'
      if self.tail["domino"]["value"].y > (self.height - 150) - self.player.height and self.directionTail == 'down':
        self.directionTail = 'right'
      elif self.tail["domino"]["value"].x > self.width - self.player.height - 25 and self.directionTail == 'right':
        self.directionTail = 'up'
        

  def play(self):
    self.board = []
    self.plus = 1
    self.plusT = 1
    self.plusF = 1
    self.turn = 1
    self.direction_play = 'up'
    self.directionHead = "up"
    self.directionTail = "down"
    self.box = Dominos()
    self.box.generate()
    self.head =  { "name": "", "domino": ""}
    self.tail =  { "name": "", "domino": ""}
    self.doubleSix = "6-6"
    self.box.shuffle()
    self.player.getDominos(self.box.dominos)
    self.machine.getDominos(self.box.dominos)

    self.outputDoubleSix(self.player)
    if len(self.player.dominos) < len(self.machine.dominos): 
      self.turn = 0
    else: 
      self.outputDoubleSix(self.machine)
      self.turn = 1
    
    self.hand()
    self.refreshGame()

    while True: 
      self.clock.tick(27)
      for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        
        x, y = pygame.mouse.get_pos()
        if (self.pass_btn_rect.collidepoint(x, y) or self.textRect.collidepoint(x, y) 
            or self.play_down_rect.collidepoint(x, y) or self.play_up_rect.collidepoint(x,y)
            or self.resetRect.collidepoint(x, y) or self.exitRect.collidepoint(x,y) 
            
            ):
          pygame.mouse.set_cursor(self.hand_cursor)
        else:
          pygame.mouse.set_cursor(self.arrow_cursor)
      
        for index in range(len(self.player.dominos)): 
           if self.player.dominos[index-1]["value"].collidepoint(x, y):
              pygame.mouse.set_cursor(self.hand_cursor)

        if self.turn == 1: 
          # for index in range(len(self.player.dominos)):
          #     if(self.turn == 0):
          #       break
          #     self.calculateTurnGame()

          #       if len(self.player.dominos) > 0:
          #         self.bot_play(self.player.dominos[index-1], index)
          #         # time.sleep(0.8)

          if event.type ==  pygame.MOUSEBUTTONDOWN:
            if self.pass_btn_rect.collidepoint(event.pos) or self.textRect.collidepoint(event.pos):
              self.turn = 0 
              self.win()

            if self.play_up_rect.collidepoint(event.pos):
              self.direction_play = 'up'
              self.refreshGame()


            if self.play_down_rect.collidepoint(event.pos):
              self.direction_play = 'down'
              self.refreshGame()

            if self.resetRect.collidepoint(event.pos):
              newGame = Game()
              newGame.play()

            if self.exitRect.collidepoint(event.pos):
              sys.exit()

            for index in range(len(self.player.dominos)): 
              if self.player.dominos[index-1]["value"].collidepoint(event.pos):
                if self.turn == 1:
                  self.calculateTurnGame()
                  self.player_play(self.player.dominos[index-1], index)
                  if self.directionHead == 'down':
                    self.plus = 2

             
        else:
          time.sleep(0.2)
          for index in range(len(self.machine.dominos)):
            if len(self.machine.dominos) > 0:
              if self.turn == 1: 
                break 
              self.calculateTurnGame()
              self.bot_play(self.machine.dominos[index-1], index)
             
  
      pygame.display.update()  
          
      

  
  def bot_play(self, currentDomino, index):
    #play for head
    if (currentDomino["name"][0] == self.head["name"] or 
        currentDomino["name"][2] == self.head["name"]):

        if(self.directionHead == 'up'): 
          currentDomino["value"].x = self.head["domino"]["value"].x
          currentDomino["value"].y = self.head["domino"]["value"].y - self.player.width if currentDomino["name"][0] == currentDomino["name"][2] else int(self.head["domino"]["value"].y) - self.player.height

          if currentDomino["name"][2] == self.head["name"]: 
            if currentDomino["name"][0] == currentDomino["name"][2]:
              currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
            else: 
                currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 180)
          
            self.head = {
              "name": currentDomino["name"][0],
              "domino": currentDomino
              }
          else:
            self.head = {
              "name": currentDomino["name"][2],
              "domino": currentDomino
              }
        elif(self.directionHead == 'left'):
          currentDomino["value"].y = self.head["domino"]["value"].y 
          currentDomino["value"].x= self.head["domino"]["value"].x - self.player.width  if currentDomino["name"][0] == currentDomino["name"][2] else int(self.head["domino"]["value"].x) - self.player.height
          
          currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], -90)

          if currentDomino["name"][2] == self.head["name"]: 
            if currentDomino["name"][0] == currentDomino["name"][2]:
              currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
            self.head = {
              "name": currentDomino["name"][0],
              "domino": currentDomino
            }
          else:
            currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 180)
            self.head = {
              "name": currentDomino["name"][2],
              "domino": currentDomino
            }

      
        elif (self.directionHead == 'down'): 
          currentDomino["value"].x = self.head["domino"]["value"].x
          currentDomino["value"].y = (self.head["domino"]["value"].y + self.player.height) if currentDomino["name"][0] == currentDomino["name"][2] and self.plus == 2 else self.head["domino"]["value"].y + self.player.width
          if currentDomino["name"][0] == self.head["name"]: 
              if currentDomino["name"][0] == currentDomino["name"][2]:
                currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
              else: 
                currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 180)

              self.head = {
                "name": currentDomino["name"][2],
                "domino": currentDomino
              }
          else:
              self.head = {
              "name": currentDomino["name"][0],
              "domino": currentDomino
              }
          
            
        self.screen.blit(currentDomino["valueSurface"] , currentDomino["value"])
        self.board.append(currentDomino)

        if self.turn == 1:
          self.player.dominos.pop(index-1)
        else:
          self.machine.dominos.pop(index-1)

        self.turn = 1 if self.turn != 1 else 0
        self.refreshGame()
        self.win()

      
    #play for tail
    elif (currentDomino["name"][0] == self.tail["name"] or 
          currentDomino["name"][2] == self.tail["name"]):
            if(self.directionTail == "down"):
              currentDomino["value"].x = self.tail["domino"]["value"].x

              if(self.plusT == 1 or self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].y = self.tail["domino"]["value"].y + self.player.width
                self.plusT = 2 
                
              elif(currentDomino["name"][0] == currentDomino["name"][2]):
                currentDomino["value"].y = self.tail["domino"]["value"].y + self.player.height
    
              else:
                currentDomino["value"].y = self.tail["domino"]["value"].y + self.player.height        
                
                
              if currentDomino["name"][0] == self.tail["name"]: 
                if currentDomino["name"][0] == currentDomino["name"][2]:
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
                else: 
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], -180)

                self.tail = {
                "name": currentDomino["name"][2],
                "domino": currentDomino
                }
              else:
                self.tail = {
                "name": currentDomino["name"][0],
                "domino": currentDomino
                }
            elif(self.directionTail == "right"):
              currentDomino["value"].y =  (self.tail["domino"]["value"].y + self.player.width) if self.plusF == 1 and not (self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]) else self.tail["domino"]["value"].y
              self.plusF = 2
              # currentDomino["value"].x =  self.tail["domino"]["value"].x + self.player.width if currentDomino["name"][0] == currentDomino["name"][2] else self.tail["domino"]["value"].x + self.player.height
              
              if(self.plusF == 1 and not self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.width

              elif(self.plusF == 1 and self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.height
                self.plusT = 2 
                
              elif(currentDomino["name"][0] == currentDomino["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.height

              elif(self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.width
                
              else:
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.height        
              
              if currentDomino["name"][0] == self.tail["name"]: 
                if currentDomino["name"][0] == currentDomino["name"][2]:
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 0)
                else: 
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], -90)
                self.tail = {
                "name": currentDomino["name"][2],
                "domino": currentDomino
                }
              else:
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
                  self.tail = {
                  "name": currentDomino["name"][0],
                  "domino": currentDomino
                  }

            self.screen.blit(currentDomino["valueSurface"] , currentDomino["value"])
            self.board.append(currentDomino)
          
            if self.turn == 1:
              self.player.dominos.pop(index-1)
            else:
              self.machine.dominos.pop(index-1)

            self.turn = 1 if self.turn != 1 else 0
            self.refreshGame()
          
    else: 
      if ((self.turn == 0 and int(index + 1) == (len(self.machine.dominos))) == True):
        self.turn = 1
      self.refreshGame()
      self.win()

  def player_play(self, currentDomino, index):
    #play for head
    if (currentDomino["name"][0] == self.head["name"] and self.direction_play == 'up'  or 
        currentDomino["name"][2] == self.head["name"] and self.direction_play == 'up' ):

        if(self.directionHead == 'up'): 
          currentDomino["value"].x = self.head["domino"]["value"].x
          currentDomino["value"].y = self.head["domino"]["value"].y - self.player.width if currentDomino["name"][0] == currentDomino["name"][2] else int(self.head["domino"]["value"].y) - self.player.height

          if currentDomino["name"][2] == self.head["name"]: 
            if currentDomino["name"][0] == currentDomino["name"][2]:
              currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
            else: 
                currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 180)
          
            self.head = {
              "name": currentDomino["name"][0],
              "domino": currentDomino
              }
          else:
            self.head = {
              "name": currentDomino["name"][2],
              "domino": currentDomino
              }
        elif(self.directionHead == 'left'):
          currentDomino["value"].y = self.head["domino"]["value"].y 
          currentDomino["value"].x= self.head["domino"]["value"].x - self.player.width  if currentDomino["name"][0] == currentDomino["name"][2] else int(self.head["domino"]["value"].x) - self.player.height
          
          currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], -90)

          if currentDomino["name"][2] == self.head["name"]: 
            if currentDomino["name"][0] == currentDomino["name"][2]:
              currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
            self.head = {
              "name": currentDomino["name"][0],
              "domino": currentDomino
            }
          else:
            currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 180)
            self.head = {
              "name": currentDomino["name"][2],
              "domino": currentDomino
            }

      
        elif (self.directionHead == 'down'): 
          currentDomino["value"].x = self.head["domino"]["value"].x
          currentDomino["value"].y = (self.head["domino"]["value"].y + self.player.width) if currentDomino["name"][0] == currentDomino["name"][2] and self.plus == 2 else self.head["domino"]["value"].y + self.player.height
          if currentDomino["name"][0] == self.head["name"]: 
              if currentDomino["name"][0] == currentDomino["name"][2]:
                currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
              else: 
                currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 180)

              self.head = {
                "name": currentDomino["name"][2],
                "domino": currentDomino
              }
          else:
              self.head = {
              "name": currentDomino["name"][0],
              "domino": currentDomino
              }
          
            
        self.screen.blit(currentDomino["valueSurface"] , currentDomino["value"])
        self.board.append(currentDomino)

        if self.turn == 1:
          self.player.dominos.pop(index-1)
        else:
          self.machine.dominos.pop(index-1)

        self.turn = 1 if self.turn != 1 else 0
        self.refreshGame()
        self.win()
      
    #play for tail
    elif (currentDomino["name"][0] == self.tail["name"] and self.direction_play == 'down'  or 
          currentDomino["name"][2] == self.tail["name"] and self.direction_play == 'down'):
            if(self.directionTail == "down"):
              currentDomino["value"].x = self.tail["domino"]["value"].x

              if(self.plusT == 1 or self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].y = self.tail["domino"]["value"].y + self.player.width
                self.plusT = 2 
                
              elif(currentDomino["name"][0] == currentDomino["name"][2]):
                currentDomino["value"].y = self.tail["domino"]["value"].y + self.player.height
    
              else:
                currentDomino["value"].y = self.tail["domino"]["value"].y + self.player.height        
                
                
              if currentDomino["name"][0] == self.tail["name"]: 
                if currentDomino["name"][0] == currentDomino["name"][2]:
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
                else: 
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], -180)

                self.tail = {
                "name": currentDomino["name"][2],
                "domino": currentDomino
                }
              else:
                self.tail = {
                "name": currentDomino["name"][0],
                "domino": currentDomino
                }
            elif(self.directionTail == "right"):
              currentDomino["value"].y =  self.tail["domino"]["value"].y + self.player.width if self.plusF == 1 and not (self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]) else self.tail["domino"]["value"].y
              self.plusF = 2
              # currentDomino["value"].x =  self.tail["domino"]["value"].x + self.player.width if currentDomino["name"][0] == currentDomino["name"][2] else self.tail["domino"]["value"].x + self.player.height
              
              if(self.plusF == 1 and not self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.width

              elif(self.plusF == 1 and self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.height
                self.plusT = 2 
                
              elif(currentDomino["name"][0] == currentDomino["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.height

              elif(self.tail["domino"]["name"][0] == self.tail["domino"]["name"][2]):
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.width
                
              else:
                currentDomino["value"].x = self.tail["domino"]["value"].x + self.player.height        
              
              if currentDomino["name"][0] == self.tail["name"]: 
                if currentDomino["name"][0] == currentDomino["name"][2]:
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 0)
                else: 
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], -90)
                self.tail = {
                "name": currentDomino["name"][2],
                "domino": currentDomino
                }
              else:
                  currentDomino["valueSurface"] = pygame.transform.rotate(currentDomino["valueSurface"], 90)
                  self.tail = {
                  "name": currentDomino["name"][0],
                  "domino": currentDomino
                  }

            self.screen.blit(currentDomino["valueSurface"] , currentDomino["value"])
            self.board.append(currentDomino)
          
            if self.turn == 1:
              self.player.dominos.pop(index-1)
            else:
              self.machine.dominos.pop(index-1)

            self.turn = 1 if self.turn != 1 else 0
            self.refreshGame()
            self.win()
    else: 
      if ((self.turn == 0 and int(index + 1) == (len(self.machine.dominos))) == True):
        self.turn = 1
      else:
        pass

      self.refreshGame()
      self.win()

#newGame = Game()
#newGame.play()