import pygame
import time

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load("../data/083_trippy-ringysnarebeat-3bars.mp3")
pygame.mixer.music.play()
print ("after music plays")
time.sleep(2)