# -*- coding: utf-8 -*-
import pygame
import math

def main():
    pygame.init()

    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("You are the King!")

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    background = pygame.image.load("Blackjack.jpg").convert()
    background = pygame.transform.scale(background, (640, 480))
    card = pygame.image.load("card.png")
    card = card.convert_alpha()
    card = pygame.transform.scale(card, (75, 100))

    card_x, card_y = 0, 200
    speed = 7
    angle_degrees = 0
    angle_radians = math.radians(angle_degrees)
    
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        angle_degrees += 1
        if angle_degrees >= 360:
            angle_degrees -= 360
        angle_radians = math.radians(angle_degrees)

        d_x = speed * math.cos(angle_radians)
        d_y = speed * math.sin(angle_radians)

        card_x += d_x
        card_y += d_y

        if card_x <= 0 or card_x >= screen_width - card.get_width():
            angle_degrees = 180 - angle_degrees
            angle_radians = math.radians(angle_degrees)

        if card_y <= 0 or card_y >= screen_height - card.get_height():
            angle_degrees = -angle_degrees
            angle_radians = math.radians(angle_degrees)

        screen.blit(background, (0, 0))
        rotated_card = pygame.transform.rotate(card, angle_degrees)
        screen.blit(rotated_card, (card_x, card_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


