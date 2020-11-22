import pygame

from game import Game
pygame.init()


## Note: Change windows size
## Note: Found another methode to display background with For or If

#Change title and size of windows
pygame.display.set_caption("Mcgyver")
screen = pygame.display.set_mode((900, 560))

#import img of background from folder
background = pygame.image.load('ressource/background.png')

#import img of game

game = Game()
#Open windows
my_windows = True

#Condition to close windows
## Note: Change condition and replace when player win

##while running = True you play
##If running = False display you win or lose
while my_windows:

    screen.blit(pygame.transform.scale(background, (50, 50)), (450, 50))
    screen.blit(pygame.transform.scale(background, (50, 50)), (395, 50))
    screen.blit(pygame.transform.scale(background, (50, 50)), (340, 50))
    screen.blit(pygame.transform.scale(background, (50, 50)), (450, 105))
    screen.blit(pygame.transform.scale(background, (50, 50)), (395, 105))
    screen.blit(pygame.transform.scale(background, (50, 50)), (340, 105))
    screen.blit(pygame.transform.scale(background, (50, 50)), (450, 160))
    screen.blit(pygame.transform.scale(background, (50, 50)), (395, 160))
    screen.blit(pygame.transform.scale(background, (50, 50)), (340, 160))

    #import img of player from folder
    screen.blit(game.player.image, game.player.rect)

    screen.blit(game.items.image, game.items.rect)

    #diplay pygame picture
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            my_windows = False
            pygame.quit()
        #detect arrow keypad
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
                print("droite")
            elif event.key == pygame.K_LEFT:
                game.player.move_left()
                print("gauche")
            elif event.key == pygame.K_UP:
                game.player.move_up()
                print("haut")
            elif event.key == pygame.K_DOWN:
                game.player.move_down()
                print("down")