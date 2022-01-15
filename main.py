import pygame
import time


class ColourSquare:
    def __init__(self, coordinates, screen):
        running = True
        white = (255, 255, 255)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = x - x % 40 + 20
                    y = y - y % 40 + 20
                    if [x, y] not in coordinates:
                        coordinates.append([x, y])
                    elif [x, y] in coordinates:
                        coordinates.remove([x, y])
                    color = pygame.Surface.get_at(screen, (x, y))
                    if color == white:
                        square = image.get_rect(center=(x, y))
                        screen.blit(image, square)
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(scr, (255, 255, 255), (x - 20, y - 20, 39, 39))
                        pygame.display.flip()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_1]:
                        NextStage(1, coordinates, screen)
                    elif pygame.key.get_pressed()[pygame.K_2]:
                        NextStage(2, coordinates, screen)
                    else:
                        MoveCamera(screen, coordinates, 1)
        pygame.quit()


class NextStage:
    def __init__(self, one_two, coordinates, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_1]:
                    NextStage(1, coordinates, screen)
                elif pygame.key.get_pressed()[pygame.K_2]:
                    NextStage(2, coordinates, screen)
                else:
                    MoveCamera(screen, coordinates, one_two)
        new_coordinates = []
        for cur in coordinates:
            temp = [[cur[0], cur[1]],
                    [cur[0] + 40, cur[1]],
                    [cur[0], cur[1] + 40],
                    [cur[0] - 40, cur[1]],
                    [cur[0], cur[1] - 40],
                    [cur[0] + 40, cur[1] + 40],
                    [cur[0] - 40, cur[1] - 40],
                    [cur[0] - 40, cur[1] + 40],
                    [cur[0] + 40, cur[1] - 40]]
            for a in temp:
                counter = 0
                for b in coordinates:
                    if a[0] == b[0] and a[1] == b[1] + 40:
                        counter += 1
                    elif a[0] == b[0] and a[1] == b[1] - 40:
                        counter += 1
                    elif a[0] == b[0] + 40 and a[1] == b[1]:
                        counter += 1
                    elif a[0] == b[0] - 40 and a[1] == b[1]:
                        counter += 1
                    elif a[0] == b[0] + 40 and a[1] == b[1] + 40:
                        counter += 1
                    elif a[0] == b[0] - 40 and a[1] == b[1] - 40:
                        counter += 1
                    elif a[0] == b[0] + 40 and a[1] == b[1] - 40:
                        counter += 1
                    elif a[0] == b[0] - 40 and a[1] == b[1] + 40:
                        counter += 1
                if a == cur:
                    if 2 <= counter <= 3:
                        new_coordinates.append(a)
                else:
                    if counter == 3:
                        new_coordinates.append(a)
        coordinates.sort()
        temp = []
        for x in new_coordinates:
            if x not in temp:
                temp.append(x)
        new_coordinates = temp
        new_coordinates.sort()
        time.sleep(0.2)
        if coordinates != new_coordinates and new_coordinates != []:
            Show(coordinates, new_coordinates, screen, one_two)
        else:
            ColourSquare(new_coordinates, screen)


class Show:
    def __init__(self, coordinates, new_coordinates, screen, one_two):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN]:
                    MoveCamera(screen, coordinates, one_two)
                elif pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                    MoveCamera(screen, coordinates, one_two)
        white = (255, 255, 255)
        for cur in coordinates:
            pygame.draw.rect(screen, white, (cur[0] - 20, cur[1] - 20, 39, 39))
        for cur in new_coordinates:
            square = image.get_rect(center=(cur[0], cur[1]))
            screen.blit(image, square)
        pygame.display.flip()
        if one_two == 1:
            ColourSquare(new_coordinates, screen)
        elif one_two == 2:
            NextStage(2, new_coordinates, screen)


class MoveCamera:
    def __init__(self, screen, coordinates, one_two):
        if pygame.key.get_pressed()[pygame.K_UP]:
            new_coordinates = []
            for cur in coordinates:
                temp1 = cur[0]
                temp2 = cur[1] + 40
                new_coordinates.append([temp1, temp2])
            Show(coordinates, new_coordinates, screen, one_two)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            new_coordinates = []
            for cur in coordinates:
                temp1 = cur[0]
                temp2 = cur[1] - 40
                new_coordinates.append([temp1, temp2])
            Show(coordinates, new_coordinates, screen, one_two)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            new_coordinates = []
            for cur in coordinates:
                temp1 = cur[0] + 40
                temp2 = cur[1]
                new_coordinates.append([temp1, temp2])
            Show(coordinates, new_coordinates, screen, one_two)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            new_coordinates = []
            for cur in coordinates:
                temp1 = cur[0] - 40
                temp2 = cur[1]
                new_coordinates.append([temp1, temp2])
            Show(coordinates, new_coordinates, screen, one_two)


pygame.init()
width = 960
height = 540
scr = pygame.display.set_mode([width, height])
scr.fill((0, 100, 0))
coordinate = []
for q in range(0, width, 40):
    for w in range(0, height, 40):
        pygame.draw.rect(scr, (255, 255, 255), (q, w, 39, 39))
pygame.display.flip()
image = pygame.image.load('photos/tetris-block.png')
ColourSquare(coordinate, scr)
