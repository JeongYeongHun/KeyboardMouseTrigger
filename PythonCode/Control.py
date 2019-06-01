import pygame

def control(keylist, stack):
    windowwidth = 100
    windowheight = 100
    pygame.init()
    pygame.display.init()
    #screen = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((windowwidth, windowheight))
    pygame.display.flip()
    clock = pygame.time.Clock()

    done = True

    while done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for index, i in enumerate(keylist):
                    if pygame.key.name(event.key) == i:
                        stack[index] = 1
                if event.key == 279:    #end
                    done = False
            if event.type == pygame.KEYUP:
                for index, i in enumerate(keylist):
                    if pygame.key.name(event.key) == i:
                        stack[index] = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                lclick, m, rclick = pygame.mouse.get_pressed()
                if lclick == 1:
                    stack[13] = 1
                if rclick == 1:
                    stack[14] = 1
            if event.type == pygame.MOUSEBUTTONUP:
                lclick, m, rclick = pygame.mouse.get_pressed()
                if lclick == 0:
                    stack[13] = 0
                if rclick == 0:
                    stack[14] = 0
            
                        
        print(stack)
    pygame.quit()
