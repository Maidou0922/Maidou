#coding=utf-8

import pygame
import time

image_filename = "C:/Users/xieTianDeThinkPad/Desktop/beach_ball.png"

pygame.init()
screen = pygame.display.set_mode((640, 480)) 
screen.fill([255, 255, 255])                  # R G B , Why use the 255 for the color ?

myBall = pygame.image.load(image_filename)   

x, y = 0, 0

position = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}
count = 0
tmpx, tmpy = 0, 0

screen.fill((255,255,255))
screen.blit(myBall, (x, y))
pygame.display.update()

while True:     # Loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # window is closed
            print("quit!!!!!!!!!!")
            exit()
            
        if event.type == pygame.KEYDOWN: #press down
            if event.key in position:
                print(event.key, "down")
                position[event.key] = 1
            elif event.key == pygame.K_a:
                print("you press a key")
                print("key", event.key) 
        elif event.type == pygame.KEYUP: #up
            if event.key in position:
                print (event.key, "up")
                position[event.key] = 0
    
    x -= position[pygame.K_LEFT]
    x += position[pygame.K_RIGHT]
    y -= position[pygame.K_UP]
    y += position[pygame.K_DOWN]
    count +=1
    #print (x,y,tmpx,tmpy, count)
    
        #print("show",x,y)
    tmpx, tmpy = x, y
    screen.fill((255,255,255))
    screen.blit(myBall, (x, y))
        
    pygame.display.update()
        