#!/usr/bin/env python3

import pygame, pygame.locals, datetime

def run():
    pygame.init()
    
    end_time = datetime.datetime(2019,7,23,12,30,0)
    # make the window, giving the size x,y
    screen = pygame.display.set_mode((200,200))

    background = pygame.image.load("background.png").convert()
    screen.blit(background,(0,0))

    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    text_colour = (0, 128, 255)
    textsurface = myfont.render('Countdown begins', False, text_colour)
    # use screen.blit to put the text onto the window
    screen.blit(textsurface,(0,0))
    # then display the current window - ask Baz about Double Buffering
    pygame.display.flip()
    pygame.time.wait(1000)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    # set the clock so it updates 
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        # rotate the logo and then calculate how much to trim it
        rotated_background = pygame.transform.rotate(background, 6*datetime.datetime.now().second)
        orig_width = background.get_width()
        width = rotated_background.get_width()  # rotating makes it bigger, so need to trim it
        margin = int((width - orig_width)/2)
        # draw it trimmed
        screen.blit(rotated_background,(0,0),(margin,margin,orig_width,orig_width))
        
        # now get the time difference, which looks like '139 days, 19:32:55.711732'
        # then divide it into two partts by splitting it at the ","
        # then find the decimal point and show the time up to the decimal point
        text_to_show = str(end_time - datetime.datetime.now())
        parts = text_to_show.split(", ") # split the days from the hours etc
        dot_position = parts[1].find(".") # look for the decimalplace to remove the microseconds
        second_line = parts[1][:dot_position + 2]  # we take the dot and teh first digit after it
        firsttextsurface = myfont.render(parts[0].encode(), False, text_colour)
        secondtextsurface = myfont.render(second_line.encode(), False, text_colour)
        screen.blit(firsttextsurface,(10,50))
        screen.blit(secondtextsurface,(10,120))
        pygame.display.flip()
        # check to see if the window has been closed
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT or event.type == pygame.locals.KEYDOWN:
                running = False
        clock.tick(20)
    pygame.quit()

if __name__ == "__main__":
    run()
