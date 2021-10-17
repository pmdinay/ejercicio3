# Import a library of functions called 'pygame'
import pygame
from main_functions import *
import math
from defines import*
# Initialize the game engine
pygame.init()

#Size changes
size = [1300, 600]# Define size of windows
titulo = input("titulo del simulador: ")
alto = int(input("Introducir alto de la ventana: "))
ancho = int(input("Introducir ancho de la ventana: "))
size[0] = alto
size[1] = ancho
red = (255, 0, 0)
#call main routine
main2(size, titulo, red)

