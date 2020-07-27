import random
import pygame
import math

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

# Caption and Icon
pygame.display.set_caption("Car Racing")


# SCORE
scoreVal = 0
font = pygame.font.Font("Generating Script Font.ttf", 32)
textY = 15
textX = 670


def showScore():
    score = font.render("SCORE: " + str(scoreVal), True, (255, 0, 5))
    screen.blit(score, (textX, textY))


game = pygame.font.Font("Generating Script Font.ttf", 64)


def GameOver():
    gameOver = game.render("GAME OVER !", True, (0, 0, 255))
    screen.blit(gameOver, (260, 250))


# PLAYER CAR

playerImg = pygame.transform.scale2x(pygame.image.load("car.png"))
playerX = 370
playerY = 480
playerVel = 3


def player():
    screen.blit(playerImg, (playerX, playerY))


# movement booleans
right = False
left = False


# side restrictions
def sides(x):
    if x <= 110 or x >= 632:
        return True
    return False


# MID OF ROAD
mid = 0


class MIDDLE:
    def __init__(self):
        midImg = pygame.image.load("minus.png")
        self.img = pygame.transform.rotate(midImg, 90)

    def draw(self, x, y):
        screen.blit(self.img, (x, y))


middleArray = []
for i in range(9):
    middleArray.append(MIDDLE())


# Car obstacle 1

car1Img = pygame.image.load("taxi.png")
car1X = random.randint(200, 550)
car1Y = random.randint(10, 20)
car1Vel = 3
car1Present = True


def car1():
    screen.blit(car1Img, (car1X, car1Y))


# Car obstacle 2

car2Img = pygame.image.load("f1.png")
car2X = random.randint(200, 550)
car2Y = random.randint(10, 20)
car2Vel = 3
car2Present = False


def car2():
    screen.blit(car2Img, (car2X, car2Y))


# Car obstacle 3

car3Img = pygame.image.load("police-car.png")
car3X = random.randint(200, 550)
car3Y = random.randint(10, 30)
car3Vel = 3
car3Present = False


def car3():
    screen.blit(car3Img, (car3X, car3Y))


grassImg = pygame.image.load("grass.jpg")


def grass(x, y):
    screen.blit(grassImg, (x, y))


end = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not sides(playerX):
                    playerX -= 5
                    left = True
                    right = False
            if event.key == pygame.K_RIGHT:
                if not sides(playerX + 32):
                    playerX += 5
                    right = True
                    left = False

    # screen color
    screen.fill((0, 0, 0))

    # GRASS
    grass(0, 0)
    grass(100, 0)
    grass(700, 0)
    grass(600, 0)

    # ROAD
    pygame.draw.polygon(screen, (180, 180, 180), ((200, 0), (100, 600), (700, 600), (600, 0)))

    # MIDDLE MOVEMENT
    j = -80
    for i in range(9):
        middleArray[i].draw(368, mid + j)
        j += 80
    mid += 2
    if mid + j >= 720:
        mid = 0

    # auto movement of player
    if not end:
        if right:
            if not sides(playerX + playerVel):
                playerX += playerVel
        if left:
            if not sides(playerX - playerVel):
                playerX -= playerVel

    # MAKING OF CARS
        if car1Present:
            car1()
            car1Y += car1Vel
        if car2Present:
            car2()
            car2Y += car2Vel
        if car3Present:
            car3()
            car3Y += car3Vel

        if car1Y >= 200:
            car2Present = True
        if car2Y >= 200:
            car3Present = True
        if car3Y >= 200:
            car1Present = True

    # RE-SPAWNING OF CARS
        if car1Y >= 950:
            car1X = random.randint(200, 550)
            car1Y = random.randint(10, 20)
            car1Vel += 1
            car1Present = True
            car2X = random.randint(200, 550)
            car2Y = random.randint(10, 20)
            car2Vel += 1
            car2Present = False
            car3X = random.randint(200, 550)
            car3Y = random.randint(10, 20)
            car3Vel += 1
            car3Present = False
            scoreVal += 10

    # COLLISION DETECTION
    if 64 >= math.sqrt((playerX - car1X) ** 2 + (playerY - car1Y) ** 2):
        GameOver()
        textX = 330
        textY = 320
        showScore()
        end = True
    if 64 >= math.sqrt((playerX - car2X) ** 2 + (playerY - car2Y) ** 2):
        GameOver()
        textX = 330
        textY = 320
        showScore()
        end = True
    if 64 >= math.sqrt((playerX - car3X) ** 2 + (playerY - car3Y) ** 2):
        GameOver()
        textX = 330
        textY = 320
        showScore()
        end = True
    if not end:
        player()

    showScore()
    clock.tick(30)

    pygame.display.update()
