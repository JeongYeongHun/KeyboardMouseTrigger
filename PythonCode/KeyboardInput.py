import pygame

windowwidth = 0
windowheight = 0
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
pygame.display.flip()
clock = pygame.time.Clock()

stack = [0, 0]
done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 97:
                stack[0] = 1
            if event.key == 304:
                stack[1] = 1
            if event.key == 279:
                done = False
        if event.type == pygame.KEYUP:
            if event.key == 97:
                stack[0] = 0
            if event.key == 304:
                stack[1] = 0

    print(stack)
pygame.quit()
