import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
screen.fill((255, 147, 48))
pygame.display.set_caption("Ciclo básico de pygame")

pygame.font.init()