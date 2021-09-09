#import py_compile 
#py_compile.compile("snake game.py")

import pygame, sys, time, random

#check error game

check_errors = pygame.init()
if check_errors[1] > 0 :
    print('[!]{check_errors} error game')
else:
    print('[+] Game sukses install')

#window game
size_x = 720
size_y = 480

#tittle game
pygame.display.set_caption('Snake game')
screen = pygame.display.set_mode((size_x, size_y))

#game variable
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255,255)
green = pygame.Color(0,255,0)

#snake
snake_pos = [100,50]
snake_body = [[100,50],[90,50],[80,50]]
change_to = "RIGHT"
direction = "RIGHT"

#food snake
food_pos = [random.randrange(1, size_x // 10) *10,random.randrange(1, size_y // 10) *10 ]

food_spawn = True

#score
score = 0

#sound
pygame.mixer.init()
eating = pygame.mixer.Sound('eatsong.wav')


# game over funct
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size_x/2, size_y/4)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    # show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

# show score funct
def show_score():
    score_font = pygame.font.SysFont('consolas', 20)
    score_surface = score_font.render('Your poin:' + str(score), True, black)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (72, 15)

    screen.blit(score_surface, score_rect)
    pygame.display.flip()


#change background to white
screen.fill(white)


#looping

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
    
    #update screen to white again
    screen.fill(white)
    
    #create snake
    for pos in snake_body:

        pygame.draw.ellipse(screen,green, pygame.Rect(pos[0],pos[1],10,10))
    
    snake_body.insert(0, snake_pos[:])
    #snake_body.pop()

    #snake run
    #fix sure move
   
    if change_to == "RIGHT" and direction !="LEFT":
       direction = "RIGHT"
    if change_to == "LEFT" and direction !="RIGHT":
       direction = "LEFT"
    if change_to == "UP" and direction !="DOWN":
       direction = "UP"
    if change_to == "DOWN" and direction !="UP":
       direction = "DOWN"

    #=======================================================
    
    if direction == "RIGHT":
       snake_pos[0] += 10
    if direction == "LEFT":
       snake_pos[0] -= 10
    if direction == "UP":
       snake_pos[1] -= 10
    if direction == "DOWN":
       snake_pos[1] += 10
    
    #snake over window
    
    if snake_pos[0] > size_x:
        snake_pos[0] = 0
    if snake_pos[0] < 0:
        snake_pos[0] = size_x
    if snake_pos[1] > size_y:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[0] = size_y


    #print(food_pos)

    #draw food
    pygame.draw.rect(screen, green, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    #snake eating food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        #print('snake eating')
        food_spawn = False
        score +=1
        eating.play()
    else:
        snake_body.pop()

    #logic food spawn
    if not food_spawn:   
        food_pos = [random.randrange(1, size_x // 10) *10,random.randrange(1, size_y // 10) *10 ]
    food_spawn = True
    #print(score)

    #show score
    show_score()

    #game over
    #print(snake_body)
    for block in snake_body:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()


    #level 
    pygame.time.Clock().tick(10)

    #update screen
    pygame.display.update()
