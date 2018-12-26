import pygame
import time

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load("../data/01_test.mp3")
pygame.mixer.music.play()
print ("Music started")
while (pygame.mixer.music.get_busy()):
    print ("Still playing")
    time.sleep(0.25)
print ("Music finished")