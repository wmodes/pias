import pygame
import time

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
effect = pygame.mixer.Sound('../data/machine_beep.wav')
effect = pygame.mixer.Sound('../data/beep_with_noisy_silent_tail.wav')
effect.play()

time.sleep(5)