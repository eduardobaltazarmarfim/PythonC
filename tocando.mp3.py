import pygame

pygame.init()

pygame.mixer.music.load('videoplayback.mp3')

pygame.mixer.music.play()
pygame.event.wait()