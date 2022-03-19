# Um programa que toca a musica selecionada na area de trabalho #

import pygame

pygame.init()
#Nome da música baixada na area de trabalho deve ser trocada logo a baixo#
pygame.mixer.music.load('CBJR.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
