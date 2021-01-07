import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Phone number checker")
clock = pygame.time.Clock()
box = pygame.Rect(175, 150, 200, 40)
reset_box = pygame.Rect(225, 400, 75, 40)

def runit():
    number = ''
    font = pygame.font.SysFont("arial", 30)
    running = True
    active = False
    while running:
        screen.fill((200, 0, 0))
        screen.blit(font.render("Enter the phone number with prefix", True, (0, 0, 0)), (80, 50))
        screen.blit(font.render("        and press enter.", True, (0, 0, 0)), (130, 90))
        pygame.draw.rect(screen, (255, 255, 255), box, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if box.collidepoint(mx, my):
                    active = True
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        running = True
                        while running:
                            # pygame.draw.rect(screen, (0, 0, 0), reset_box, 0)
                            screen.blit(font.render("Reset", True, (255, 255, 255)), (230, 405))
                            numbers = str(number)
                            text3 = font.render("Checking number.. " + str(number), True, (0, 0, 0))
                            screen.blit(text3, (50, 200))
                            ch_number = phonenumbers.parse(numbers, "CH")
                            text1 = font.render("Country: " + geocoder.description_for_number(ch_number, "en"), True, (0, 0, 0))
                            screen.blit(text1, (100, 240))
                            pygame.time.wait(100)
                            ro_number = phonenumbers.parse(numbers, "RO")
                            text2 = font.render("Operator: " + carrier.name_for_number(ro_number, "en"), True, (0, 0, 0))
                            screen.blit(text2, (100, 280))
                            time = font.render("TimeZone: " + str(timezone.time_zones_for_number(ch_number)), True, (0, 0, 0))
                            screen.blit(time, (50, 320))
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    quit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mx, my = pygame.mouse.get_pos()
                                    if reset_box.collidepoint(mx, my):
                                        runit()
                    elif event.key == pygame.K_BACKSPACE:
                        number = number[:-1]
                    else:
                        number += str(event.unicode)
        text_surface = font.render(number, 1, (0, 0, 0))
        screen.blit(text_surface, (180, 155))
        pygame.display.update()
        clock.tick(5)

runit()