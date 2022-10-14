from socketserver import BaseRequestHandler
import pygame
import pygame_menu
from main import Game
import simpleaudio as sa
import time 

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.Info()
size = width, height = display.current_w, display.current_h
surface = pygame.display.set_mode((width, height))
bg_img = pygame_menu.BaseImage(image_path="img/background.jpg")

beer = pygame.image.load("img/beer.png")
beer_rect = beer.get_rect()
beer = pygame.transform.rotate(beer, -30)
beer_rect.x, beer_rect.y = width/10 , height - 500

beer2 = pygame.image.load("img/beer.png")
beer2_rect = beer2.get_rect()
beer2 = pygame.transform.rotate(beer2,30)
beer2_rect.x, beer2_rect.y = width/1.5 , height - 500


music = pygame.mixer.music.load("track1.wav")
music = pygame.mixer.music.play()
music = pygame.mixer.music.set_volume(0.4)


def main_bg():
    bg_img.draw(surface)
    surface.blit(beer, beer_rect)
    surface.blit(beer2, beer2_rect)
def start_the_game():
    time.sleep(0.0001)
    newGame = Game()
    newGame.play()  
    pass

def playmusic():
    music = pygame.mixer.music.unpause()

def stopmusic():
    music = pygame.mixer.music.pause()





menu = pygame_menu.Menu('Dominó', width/6, height/3,
                       theme=pygame_menu.themes.THEME_DARK)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.add.button('Play Music', playmusic)
menu.add.button('Stop Music', stopmusic)

menu.mainloop(surface, main_bg)
