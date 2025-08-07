import pygame    #import pygame lib for game setup
import random    #for random food position
import sys       #for system exit

pygame.init()    #intilialize pygame lib

#Screen setup
WIDTH, HEIGHT = 800, 600      #game window size
CELL_SIZE = 40                #each snake/food image size
screen = pygame.display.set_mode((WIDTH, HEIGHT))     #create window size
pygame.display.set_caption("Snake Game")           #title for the screen

#Load images
snake_img = pygame.image.load("Circle.jpg")  #snake image
snake_img = pygame.transform.scale(snake_img, (CELL_SIZE, CELL_SIZE)) #scale it to grid size

food_img = pygame.image.load("APPLE.jpg")  #apple image
food_img = pygame.transform.scale(food_img, (CELL_SIZE, CELL_SIZE)) #scale it to grid size

clock = pygame.time.Clock() #time to control the frame rate

# Snake initial position
snake = [(200, 200)]    #snake starting position
direction = "RIGHT"     #intial position of snake direction
#spawn intial food at random grid position
food_pos = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)   

#draw snake on to screen
def draw_snake():  
    for segment in snake:
        screen.blit(snake_img, segment)

#draw food on to screen
def draw_food():
    screen.blit(food_img, food_pos)

def move_snake():
    global snake
    x, y = snake[0]  #get current head position if snake(snake[0] is the head)
    #change direction of the snake based on the direction
    if direction == "UP":      
        y -= CELL_SIZE
    elif direction == "DOWN":
        y += CELL_SIZE
    elif direction == "LEFT":
        x -= CELL_SIZE
    elif direction == "RIGHT":
        x += CELL_SIZE

    #create a new head pos
    new_head = (x, y)
    snake.insert(0, new_head)  #add new head to the front of the sanke

    #check if snake eats food
    if new_head == food_pos: 
        spawn_food()    #spawn new food if eaten, snake grows 
    else:
        snake.pop() #if not, remove tail

def spawn_food():     #place food randomly within the grid
    global food_pos
    food_pos = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)

def check_collision():
    head = snake[0]  #snake head pos
    #Check self-collision
    if head in snake[1:]:
        return True
    #Check wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    return False  #no collision

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #handle keyboard input for snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":  #prevent going in opposite direction
        direction = "UP"
    elif keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    elif keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    elif keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    #move the sanke
    move_snake()

    #check if the collision is with self or wall
    if check_collision():
        print("Game Over")
        pygame.quit()
        sys.exit()   

    screen.fill((0, 0, 0))  #fills screen in black color
    draw_snake()
    draw_food()
    pygame.display.update()

    clock.tick(5)