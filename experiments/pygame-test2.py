import pygame
import time

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
sound = pygame.mixer.Sound('../data/083_trippy-ringysnarebeat-3bars.mp3')
audio = sound.play(sound)
print ("Music started")
while (audio.get_busy()):
    print ("Still playing")
    time.sleep(0.25)
print ("Music finished")