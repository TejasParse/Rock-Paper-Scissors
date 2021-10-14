import pygame
import random
import math
from pygame import event

from pygame.font import Font

pygame.init()

screen = pygame.display.set_mode((1000,800))

pygame.display.set_caption("Rock Paper Scissors")

running = True

won =0 
loss =0
draw =0
types = ["Rock","Paper","Scissors","Start the Game"]
stats = ["      Won!","      Lost","      Draw","Start the Game"]
font = pygame.font.Font("freesansbold.ttf",32)

rock_p = pygame.image.load("data/images/rock_p.png")
rock_p = pygame.transform.scale(rock_p,(300,300))
paper_p = pygame.image.load("data/images/paper_p.png")
paper_p = pygame.transform.scale(paper_p,(300,300))
scissors_p = pygame.image.load("data/images/scissors_p.png")
scissors_p = pygame.transform.scale(scissors_p,(400,300))

rock_o = pygame.image.load("data/images/rock_o.png")
rock_o = pygame.transform.scale(rock_o,(300,300))
paper_o = pygame.image.load("data/images/paper_o.png")
paper_o = pygame.transform.scale(paper_o,(300,300))
scissors_o = pygame.image.load("data/images/scissors_o.png")
scissors_o = pygame.transform.scale(scissors_o,(400,300))

player_images= [rock_p,paper_p,scissors_p,font.render("",True,(255,255,255))]
opponent_images= [rock_o,paper_o,scissors_o,font.render("",True,(255,255,255))]


status = stats[3]


def show_score():
    score = font.render("Won: "+str(won)+" Loss: "+str(loss)+" Draw: "+str(draw),True,(255,255,255))
    screen.blit(score,(20,150))


def show_player(turn):
    score = font.render("Player",True,(255,255,255))
    screen.blit(score,(150,300))
    screen.blit(player_images[turn], (75,400))

def show_opponent(turn):
    score = font.render("Opponent(Comp)",True,(255,255,255))
    screen.blit(score,(640,300))
    screen.blit(opponent_images[turn], (600,400))

def rules():
    score = font.render("R: To play Rock         P: To play Paper        S:To play Scissors ",True,(255,255,255))
    screen.blit(score,(20,20))

def show_won_loss_tie(temp):
    temp1 = font.render(temp,True,(255,255,255))
    screen.blit(temp1,(330,225))

comp=3
player=3
while running:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running=False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_r:
                player =0
                comp = random.randint(0,2)
            
                if(comp == 1):
                    loss+=1
                    status = stats[1]
                elif(comp == 2):
                    won+=1
                    status = stats[0]
                else:
                    status = stats[2]
                    draw+=1
                
              
            if i.key==pygame.K_p:
                player=1
                comp = random.randint(0,2)
                if(comp == 2):
                    status = stats[1]
                    loss+=1
                elif(comp == 0):
                    status = stats[0]
                    won+=1
                else:
                    status = stats[2]
                    draw+=1
              
              
            if i.key == pygame.K_s:
                player=2
                comp = random.randint(0,2)
                if(comp == 0):
                    status = stats[1]
                    loss+=1
                elif(comp == 1):
                    status = stats[0]
                    won+=1
                else:
                    status = stats[2]
                    draw+=1


    screen.fill((255,0,0))
    rules()
    show_score()
    show_player(player)
    show_opponent(comp)
    show_won_loss_tie(status)
    pygame.display.update()
