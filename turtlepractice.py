import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
egg = pygame.image.load('egg.png')
pygame.display.set_icon(egg)

distance_width = 800
distance_height = 600
width = distance_width/2
height = distance_height/2
game  = True

def snake(x,y):
        for i in range(4):
                screen.blit(egg, (x,y))
        
move = 0
snake_pos_x = 0
snake_pos_y = 0
snakeX = 300
snakeY = 400
count = 0
while game:
        screen.fill((255,255,255))
        count+=1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                        snake_pos_x = -5
                        snake_pos_y = 0
                if keys[pygame.K_RIGHT]:
                        snake_pos_x = 5
                        snake_pos_y = 0
                if keys[pygame.K_UP]:
                        snake_pos_y = -5
                        snake_pos_x = 0
                if keys[pygame.K_DOWN]:
                        snake_pos_y = 5
                        snake_pos_x = 0
        
        
        snakeX +=snake_pos_x
        snakeY +=snake_pos_y
        print(snake_pos_x)               
                
        snake(snakeX, snakeY)    
                
        pygame.display.update()

 
        





