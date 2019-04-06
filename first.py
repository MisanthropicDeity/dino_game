import pygame
import time

pygame.init()

display_width = 1200
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))
x = display_width*0.1
y = display_height*0.35

y_change = 0
#car_speed = 0ode((display_width,display_height))
pygame.display.set_caption('Numero Uno')

black = (0,0,0)
white = (255,255,255)
grey = (211,211,211)

clock = pygame.time.Clock()

dinoImg = pygame.image.load('dino.png')
width = dinoImg.get_width()
height = dinoImg.get_height()
print(width,height)

def tree(t_x,t_y,t_w,t_h,color):
    pygame.draw.rect(gameDisplay,color,[t_x,t_y,t_w,t_h])

def text_objects(text,font):
    textSurface = font.render(text,True,grey)
    return textSurface, textSurface.get_rect()

def Message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf , TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    Message_display('Game Over')


def dino(x,y):
    gameDisplay.blit(dinoImg,(x,y))


def game_loop():
    x = display_width * 0.15
    y = display_height * 0.55

    tree_starty = y
    tree_startx = display_width
    tree_speed  = -7
    tree_w = 50
    tree_h =70

    crashed = False


    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y+=-150
                if event.key == pygame.K_DOWN:
                    y+=+100
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y= display_height*0.45
                if event.key == pygame.K_DOWN:
                    y= display_height*0.45

        gameDisplay.fill(white)
        tree(tree_startx,tree_starty,tree_w,tree_h,grey)
        tree_startx += tree_speed

        if tree_startx < 0:
            tree_startx = display_width- tree_w
        if x < tree_startx+tree_w:
            print ("x crossover")
            if y > tree_starty and y < tree_starty+tree_h or y+height > tree_starty and y + height< tree_starty + tree_w:
                print("y crossover")
                crash()

        dino(x, y)
        #print (event)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()