import pygame
import Conduct
#import SerialToArduino

def control(keylist, stack):
    windowwidth = 300
    windowheight = 300
    pygame.init()
    pygame.display.init()
    #screen = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((windowwidth, windowheight))
    pygame.display.flip()
    clock = pygame.time.Clock()

    done = True
    screen_info = pygame.display.Info()
    dx = screen_info.current_w/2
    dy = screen_info.current_h/2
    #pygame.mouse.set_pos(dx, dy)
    #pygame.mouse.set_visible(False)
    #pygame.event.set_grab(True)
    Conduct.setStack(stack)

    while done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for index, i in enumerate(keylist):
                    if pygame.key.name(event.key) == i:
                        stack[index] = 1
                if event.key == 279:    #end
                    Conduct.endConduct()
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
            if event.type == pygame.MOUSEMOTION:
                x,y = pygame.mouse.get_rel()
                stack[18] = x
                stack[19] = y

                '''
                x,y = pygame.mouse.get_pos()
                if x < (dx/5) or y < (dy/5) or x > (dx + (dx/5)*4) or y > (dy + (dy/5)*4):
                    pygame.mouse.set_pos(dx, dy)
                    stack[18] = x-dx
                    stack[19] = y-dy
                    Conduct.setStack(stack)
                else:
                    stack[18] = x-dx
                    stack[19] = y-dy
                '''
                
            Conduct.conduct(stack)
            print(stack)
        #SerialToArduino.sendserial(stack)   #아두이노와 시리얼통신
        

        

        
    pygame.quit()
