import pygame
from pygame.locals import *
import os

pygame.init()


def what_day(Date):

    # data
    d = Date.replace(" ", "")

    Y_ear_ = d[:-6]
    Y_ear = int(Y_ear_)
    Month_ = d[-5:-3]
    Month = int(Month_)
    Day_ = d[-2:]
    Day = int(Day_)
    century_ = Y_ear_[:-2]
    century = int(century_)
    year_ = Y_ear_[-2:]
    year = int(year_)

    # Century_code
    cb4 = century / 4

    if cb4 - int(cb4) == 0.75:
        cen_code = 3
    elif cb4 - int(cb4 == 0):
        cen_code = 2
    elif cb4 - int(cb4) == 0.25:
        cen_code = 0
    elif cb4 - int(cb4) == 0.5:
        cen_code = 5

    # Doomsday_calculator
    c = cen_code
    y = int(year / 12)
    r = year % 12
    cyr = int(r / 4)
    t = c + y + r + cyr
    doomsday = t % 7
    d_d = 1

    # d_rem calculator
    if Month == 1:
        if Y_ear % 4 == 0 and Y_ear % 400 != 0:
            d_d = 4
        else:
            d_d = 3
    elif Month == 2:
        if Y_ear % 4 == 0 and Y_ear % 400 != 0:
            d_d = 29
        else:
            d_d = 28
    elif Month == 3:
        d_d = 14
    elif Month == 4:
        d_d = 4
    elif Month == 5:
        d_d = 9
    elif Month == 6:
        d_d = 6
    elif Month == 7:
        d_d = 11
    elif Month == 8:
        d_d = 8
    elif Month == 9:
        d_d = 5
    elif Month == 10:
        d_d = 10
    elif Month == 11:
        d_d = 7
    elif Month == 12:
        d_d = 12

    day_rem = (Day - d_d) % 7

    # day

    if day_rem == 0:
        dayy = doomsday
    elif day_rem == 1:
        dayy = doomsday + 1
    elif day_rem == 2:
        dayy = doomsday + 2
    elif day_rem == 3:
        dayy = doomsday + 3
    elif day_rem == 4:
        dayy = doomsday + 4
    elif day_rem == 5:
        dayy = doomsday + 5
    elif day_rem == 6:
        dayy = doomsday + 6

    dayyy = dayy % 7

    if dayyy == 0:
        return "SUNDAY"
    elif dayyy == 1:
        return "MONDAY"
    elif dayyy == 2:
        return "TUESDAY"
    elif dayyy == 3:
        return "WEDNESDAY"
    elif dayyy == 4:
        return "THURSDAY"
    elif dayyy == 5:
        return "FRIDAY"
    elif dayyy == 6:
        return "SATURDAY"


def assects_pather(filename):
    asfp = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    return os.path.join(asfp, filename)


screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Day_Teller")
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()


bg = pygame.image.load(assects_pather("bg.jpg"))


active_color = (255, 0, 0)
passive_color = (0, 0, 0)

inp_rect = pygame.Rect(50, 149, 400, 61)
inp_color = passive_color

date = font.render("Date: ", True, "Black")
frmt = font.render("YYYY/MM/DD", True, "Black")

user_in = ""

out_rect = pygame.Rect(100, 350, 300, 61)


active = False
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == VIDEORESIZE:
            pygame.display.set_mode((500, 600))

        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            if inp_rect.collidepoint(pos) and event.button == 1:
                active = True
                user_in = ""

        elif event.type == pygame.KEYDOWN:

            if event.key == K_RETURN or event.key == K_KP_ENTER:
                active = False

            elif event.key == K_BACKSPACE and active == True:
                user_in = user_in[:-1]

            else:
                if event.key < 256 and active == True:
                    key_char = chr(event.key)
                    user_in += key_char

    user_date = font.render(user_in, True, "Black")

    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, inp_color, inp_rect, 10)
    screen.blit(date, (67, 162))
    screen.blit(user_date, (175, 162))
    pygame.draw.rect(screen, "Black", out_rect, 10)

    if active == True:
        inp_color = active_color
    elif active == False:
        inp_color = passive_color

    if active == False and user_in == "":
        screen.blit(frmt, (175, 162))

    elif active == False and user_in != "":
        try:
            sys_out = font.render((what_day(user_in)), True, "Black")
            screen.blit(sys_out, (130, 363))

        except:
            user_in = ""

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
