import pygame

windowwidth = 10
windowheight = 10
pygame.init()
pygame.display.init()
#screen = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
screen = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.flip()
clock = pygame.time.Clock()

keylist = ['a', 's', 'd', '1', '']
stack = [0, 0, 0, 0, 0]
done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            for index, i in enumerate(keylist):
                if pygame.key.name(event.key) == i:
                    stack[index] = 1
            if event.key == 279:
                done = False
            print(pygame.key.name(event.key))
        if event.type == pygame.KEYUP:
            for index, i in enumerate(keylist):
                if pygame.key.name(event.key) == i:
                    stack[index] = 0
    #print(stack)
pygame.quit()
