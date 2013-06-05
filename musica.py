import pygame
import os
import sys
import pygame.mixer
import pygame.mixer.cdrom



pygame.mixer.init(44100, 16, 2 ,4096)
reload(sys)
sys.setdefaultencoding(utf8)

pygame.mixer.music.load('Damaderojo.mp3')


pygame.mixer.music.play(loops=1, start=0.0)
    

pygame.mixer.music.queue('otra/Micorazonteseguira.mp3')
pygame.mixer.music.set_volume(1.0)

pygame.mixer.music.set_endevent()
