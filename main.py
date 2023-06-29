import pygame, sys, time
from pygame.locals import *
import os

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
width = 1000
height = 765
pygame.mouse.set_visible(True)
mainSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('HINAYANA')
background = pygame.image.load('images\path.png')


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


bac = load_image('path.png')
image = load_image("start.png")
image2_1 = load_image("HINAYANA.png")
image2 = load_image('HINAYANA_1.png')
image3 = load_image('lokstart.png')
grave = load_image('graves.png')
churchs = load_image('church.png')
loung = load_image('FBhDIosWQAQ-XbS.png')
loung2 = load_image('liv.png')
loung1 = load_image('liv2.png')
insid = load_image('inside.png')
insid1 = load_image('inside1.png')
bath = load_image('bathr.png')
secre = load_image('secret.png')
slep = load_image('bedroom.png')
lette = load_image('letter.png')
book = load_image('1984_1.png')
toen = load_image('toend.png')
end1 = load_image('end1.png')
end2 = load_image('end2.png')
end3 = load_image('end3.png')
rules = load_image('rule.png')
idontk = load_image('bedrooms.png')
faren = load_image('451.png')
final = load_image('final.png')


game = True
flag = False
def start1():
    global game
    global flag
    i2 = pygame.transform.scale(bac, (1000, 765))
    background.blit(i2, (0, 0))


    all_sprites = pygame.sprite.Group()  # спрайты стартого окна

    start = pygame.sprite.Sprite()  # кнопка старт
    start.image = load_image("start.png")
    start.rect = start.image.get_rect()
    all_sprites.add(start)
    start.rect.x = 345
    start.rect.y = 260

    rules = pygame.sprite.Sprite()  # кнопка правил
    rules.image = load_image("rules.png")
    rules.rect = rules.image.get_rect()
    all_sprites.add(rules)
    rules.rect.x = 345
    rules.rect.y = 380

    all_sprites.draw(background)

    while game:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag is False and 365 <= mouse[0] <= 665 and 400 <= mouse[1] <= 500:
                    i = pygame.transform.scale(image2_1, (1000, 765))
                    background.blit(i, (0, 0))
                    flag = True
                if 365 <= mouse[0] <= 665 and 500 <= mouse[1] <= 600:
                    rule()
            if flag:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game = False
                        next()
        pygame.display.update()


def rule():
    i2 = pygame.transform.scale(rules, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start1()
        pygame.display.update()


def next():
    i2 = pygame.transform.scale(image2, (1000, 765))
    background.blit(i2, (0, 0))

    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startlock()
        pygame.display.update()


# все функции улицы
def startlock():
    i2 = pygame.transform.scale(image3, (1000, 765))
    background.blit(i2, (0, 0))
    flag = True
    while flag:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    graves()
                    flag = False
                if event.key == pygame.K_a:
                    church()
                    flag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 460 <= mouse[0] <= 565 and 34 <= mouse[1] <= 114:
                    lounge()

        pygame.display.update()


def church():
    i2 = pygame.transform.scale(churchs, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 295 <= mouse[0] <= 356 and 415 <= mouse[1] <= 485:
                    inside()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    startlock()
        pygame.display.update()


tr = True
def inside():
    global tr
    if tr:
        i2 = pygame.transform.scale(insid, (1000, 765))
        background.blit(i2, (0, 0))
    else:
        i2 = pygame.transform.scale(insid1, (1000, 765))
        background.blit(i2, (0, 0))

    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 446 <= mouse[0] <= 553 and 297 <= mouse[1] <= 326 and tr:
                    tr = False
                    font = pygame.font.Font('Shrift\GangSmallYuxian.otf', 20)
                    text = font.render('get a blessing from God (Press SPACE)', (255, 255, 255), (0, 0, 0))

                    close_window = pygame.sprite.Group()

                    window = pygame.sprite.Sprite()
                    window.image = load_image("window.png")
                    window.rect = window.image.get_rect()

                    close = pygame.sprite.Sprite()
                    close.image = load_image("close.png")
                    close.rect = close.image.get_rect()

                    close_window.add(window)
                    close_window.add(close)

                    window.rect.x = 280
                    window.rect.y = 602

                    close.rect.x = 635
                    close.rect.y = 560

                    close_window.draw(background)
                    background.blit(text, (290, 610))

                if 695 <= mouse[0] <= 718 and 612 <= mouse[1] <= 633:
                    tr = True
                    background.blit(i2, (0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    church()

                if event.key == pygame.K_SPACE and tr is False:
                    i = pygame.transform.scale(insid1, (1000, 765))
                    background.blit(i, (0, 0))
                    fp = open('god.txt', 'w')
                    fp.write('You gained a blessing of God')
                    fp.close()

        pygame.display.update()


def graves():
    i2 = pygame.transform.scale(grave, (1000, 765))
    background.blit(i2, (0, 0))
    while flag:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        close_window = pygame.sprite.Group()
        font = pygame.font.Font('Shrift\GangSmallYuxian.otf', 25)
        window = pygame.sprite.Sprite()
        window.image = load_image("window.png")
        window.rect = window.image.get_rect()

        close = pygame.sprite.Sprite()
        close.image = load_image("close.png")
        close.rect = close.image.get_rect()

        close_window.add(window)
        close_window.add(close)

        window.rect.x = 280
        window.rect.y = 602

        close.rect.x = 635
        close.rect.y = 560
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 783 <= mouse[0] <= 834 and 479 <= mouse[1] <= 536:
                    text = font.render('G. E. Timberlade 1968 - 1993', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 821 <= mouse[0] <= 869 and 303 <= mouse[1] <= 363:
                    text = font.render('L. M. Jackson 1955 - 1999', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 879 <= mouse[0] <= 933 and 651 <= mouse[1] <= 716:
                    text = font.render('H. V. Barlow 1972 - 2000', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                if 695 <= mouse[0] <= 718 and 612 <= mouse[1] <= 633:
                    background.blit(i2, (0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    startlock()

        pygame.display.update()


prosto = True
prosto1 = True
def lounge():
    global prosto
    if prosto:
        i2 = pygame.transform.scale(loung, (1000, 765))
        background.blit(i2, (0, 0))
    else:
        i2 = pygame.transform.scale(loung2, (1000, 765))
        background.blit(i2, (0, 0))

    close_window = pygame.sprite.Group()
    font = pygame.font.Font('Shrift\GangSmallYuxian.otf', 25)
    window = pygame.sprite.Sprite()
    window.image = load_image("window.png")
    window.rect = window.image.get_rect()

    close = pygame.sprite.Sprite()
    close.image = load_image("close.png")
    close.rect = close.image.get_rect()

    close_window.add(window)
    close_window.add(close)

    window.rect.x = 280
    window.rect.y = 602

    close.rect.x = 635
    close.rect.y = 560

    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 468 <= mouse[0] <= 486 and 147 <= mouse[1] <= 178:
                    kniga()

                elif 166 <= mouse[0] <= 237 and 89 <= mouse[1] <= 149 and prosto:
                    code_l()

                elif 270 <= mouse[0] <= 304 and 457 <= mouse[1] <= 484:
                    kniga2()

                elif 631 <= mouse[0] <= 648 and 192 <= mouse[1] <= 219:
                    text = font.render('Dont forget to buy red wine', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 656 <= mouse[0] <= 673 and 184 <= mouse[1] <= 209:
                    text = font.render('Dont forget to buy tomatoes', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 41 <= mouse[0] <= 56 and 392 <= mouse[1] <= 410:
                    text = font.render('+1 751 420 0919', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 173 <= mouse[0] <= 281 and 627 <= mouse[1] <= 723:
                    text = font.render('TV channel: Syfy', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 425 <= mouse[0] <= 456 and 510 <= mouse[1] <= 537:
                    text = font.render('The killer Eric Rudolph was caught', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                if 695 <= mouse[0] <= 718 and 612 <= mouse[1] <= 633:
                    background.blit(i2, (0, 0))

                if 185 <= mouse[0] <= 206 and 123 <= mouse[1] <= 136 and prosto is False:
                    text = font.render('SHE.', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    startlock()


                elif event.key == pygame.K_a:
                    dorm()

        pygame.display.update()


def code_l():
    i2 = pygame.transform.scale(loung1, (1000, 765))
    background.blit(i2, (0, 0))
    global prosto
    code = ''

    close_window = pygame.sprite.Group()
    font = pygame.font.Font('Shrift\GangSmallYuxian.otf', 25)
    window = pygame.sprite.Sprite()
    window.image = load_image("window.png")
    window.rect = window.image.get_rect()

    close = pygame.sprite.Sprite()
    close.image = load_image("close.png")
    close.rect = close.image.get_rect()

    close_window.add(window)
    close_window.add(close)

    window.rect.x = 280
    window.rect.y = 602

    close.rect.x = 635
    close.rect.y = 560

    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 468 <= mouse[0] <= 486 and 147 <= mouse[1] <= 178:
                    kniga()

                elif 270 <= mouse[0] <= 304 and 457 <= mouse[1] <= 484:
                    kniga2()

                elif 41 <= mouse[0] <= 56 and 392 <= mouse[1] <= 410:
                    text = font.render('+1 911 765 4354', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 631 <= mouse[0] <= 648 and 192 <= mouse[1] <= 219:
                    text = font.render('Dont forget to buy red wine', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 656 <= mouse[0] <= 673 and 184 <= mouse[1] <= 209:
                    text = font.render('Dont forget to buy tomatoes', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 173 <= mouse[0] <= 281 and 627 <= mouse[1] <= 723:
                    text = font.render('TV channel: Syfy', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 425 <= mouse[0] <= 456 and 510 <= mouse[1] <= 537:
                    text = font.render('The killer Eric Rudolph was caught', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                if 695 <= mouse[0] <= 718 and 612 <= mouse[1] <= 633:
                    background.blit(i2, (0, 0))

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_s:
                    startlock()

                elif event.key == pygame.K_a:
                    dorm()

                if event.key == pygame.K_0:
                    code += '0'

                if event.key == pygame.K_1:
                    code += '1'

                if event.key == pygame.K_2:
                    code += '2'

                if event.key == pygame.K_3:
                    code += '3'

                if event.key == pygame.K_4:
                    code += '4'

                if event.key == pygame.K_5:
                    code += '5'

                if event.key == pygame.K_6:
                    code += '6'

                if event.key == pygame.K_7:
                    code += '7'

                if event.key == pygame.K_8:
                    code += '8'

                if event.key == pygame.K_9:
                    code += '9'

        if code == '1984':
            prosto = False
            code = ''
            lounge()

        elif 0 < len(code) < 4:
            text = font.render(code, (255, 255, 255), (0, 0, 0))
            close_window.draw(background)
            background.blit(text, (290, 610))

        elif len(code) == 4:
            text = font.render('Try again', (255, 255, 255), (0, 0, 0))
            close_window.draw(background)
            background.blit(text, (290, 610))

            code = ''

        pygame.display.update()


def kniga():
    i2 = pygame.transform.scale(book, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 919 <= mouse[0] <= 998 and 4 <= mouse[1] <= 62:
                    lounge()

        pygame.display.update()


def kniga2():
    i2 = pygame.transform.scale(faren, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 919 <= mouse[0] <= 998 and 4 <= mouse[1] <= 62:
                    lounge()

        pygame.display.update()


def dorm():
    i2 = pygame.transform.scale(slep, (1000, 765))
    background.blit(i2, (0, 0))

    close_window = pygame.sprite.Group()
    font = pygame.font.Font('Shrift\GangSmallYuxian.otf', 25)
    window = pygame.sprite.Sprite()
    window.image = load_image("window.png")
    window.rect = window.image.get_rect()

    close = pygame.sprite.Sprite()
    close.image = load_image("close.png")
    close.rect = close.image.get_rect()

    close_window.add(window)
    close_window.add(close)

    window.rect.x = 280
    window.rect.y = 602

    close.rect.x = 635
    close.rect.y = 560

    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 726 <= mouse[0] <= 787 and 138 <= mouse[1] <= 204:
                    col()

                if 419 <= mouse[0] <= 486 and 170 <= mouse[1] <= 256:
                    text = font.render('It was not watered for 3 days', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 111 <= mouse[0] <= 244 and 26 <= mouse[1] <= 138:
                    text = font.render('De sterrennacht 1889', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                if 695 <= mouse[0] <= 718 and 612 <= mouse[1] <= 633:
                    background.blit(i2, (0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    lounge()

        pygame.display.update()


def col():
    i2 = pygame.transform.scale(idontk, (1000, 765))
    background.blit(i2, (0, 0))
    code = ''

    close_window = pygame.sprite.Group()  # группа спрайтов при нажатии на могилу
    font = pygame.font.Font('Shrift\GangSmallYuxian.otf', 25)
    window = pygame.sprite.Sprite()
    window.image = load_image("window.png")
    window.rect = window.image.get_rect()

    close = pygame.sprite.Sprite()
    close.image = load_image("close.png")
    close.rect = close.image.get_rect()

    close_window.add(window)
    close_window.add(close)

    window.rect.x = 280
    window.rect.y = 602

    close.rect.x = 635
    close.rect.y = 560

    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 419 <= mouse[0] <= 486 and 170 <= mouse[1] <= 256:
                    text = font.render('It was not watered for 3 days', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                elif 111 <= mouse[0] <= 244 and 26 <= mouse[1] <= 138:
                    text = font.render('De sterrennacht 1889', (255, 255, 255), (0, 0, 0))
                    close_window.draw(background)
                    background.blit(text, (290, 610))

                if 695 <= mouse[0] <= 718 and 612 <= mouse[1] <= 633:
                    background.blit(i2, (0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    secr()

                if event.key == pygame.K_d:
                    lounge()

                if event.key == pygame.K_0:
                    code += '0'

                if event.key == pygame.K_1:
                    code += '1'

                if event.key == pygame.K_2:
                    code += '2'

                if event.key == pygame.K_3:
                    code += '3'

                if event.key == pygame.K_4:
                    code += '4'

                if event.key == pygame.K_5:
                    code += '5'

                if event.key == pygame.K_6:
                    code += '6'

                if event.key == pygame.K_7:
                    code += '7'

                if event.key == pygame.K_8:
                    code += '8'

                if event.key == pygame.K_9:
                    code += '9'

        if code == '6414':
            secr()

        elif 0 < len(code) < 4:
            text = font.render(code, (255, 255, 255), (0, 0, 0))
            close_window.draw(background)
            background.blit(text, (290, 610))

        elif len(code) == 4:
            text = font.render('Try again', (255, 255, 255), (0, 0, 0))
            close_window.draw(background)
            background.blit(text, (290, 610))

            code = ''

        pygame.display.update()


def secr():
    i2 = pygame.transform.scale(secre, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 658 <= mouse[0] <= 698 and 386 <= mouse[1] <= 410:
                    lett()
        pygame.display.update()


def lett():
    i2 = pygame.transform.scale(lette, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    choice()

        pygame.display.update()


def choice():
    i2 = pygame.transform.scale(toen, (1000, 765))
    background.blit(i2, (0, 0))

    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 103 <= mouse[0] <= 277 and 120 <= mouse[1] <= 278:
                    end_3()
                if 103 <= mouse[0] <= 277 and 338 <= mouse[1] <= 486:
                    end_2()
                if 103 <= mouse[0] <= 277 and 553 <= mouse[1] <= 692:
                    end_1()
        pygame.display.update()


def end_1():
    i2 = pygame.transform.scale(end1, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fin()
        pygame.display.update()


def end_2():
    i2 = pygame.transform.scale(end2, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fin()
        pygame.display.update()


def end_3():
    i2 = pygame.transform.scale(end3, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fin()
        pygame.display.update()


def fin():
    global game
    global flag
    global prosto
    global prosto1
    global tr
    i2 = pygame.transform.scale(final, (1000, 765))
    background.blit(i2, (0, 0))
    while True:
        fpsClock.tick(FPS)
        mainSurface.blit(background, (0, 0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 602 and 505 <= mouse[1] <= 612:
                    game = True
                    flag = False
                    prosto = True
                    prosto1 = True
                    tr = True
                    start1()

                if 720 <= mouse[0] <= 772 and 671 <= mouse[1] <= 717:
                    fp = open('h1n4y4n4.txt', 'w')
                    fp.write('https://ru.wikipedia.org/wiki/%D0%A5%D0%B8%D0%BD%D0%B0%D1%8F%D0%BD%D0%B0')
                    fp.close()
        pygame.display.update()


start1()