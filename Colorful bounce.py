import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


class Sprite(pygame.sprite.Sprite):

    #constructor method
    def __init__(self, color, height, width):
        #call the parent class (sprite) constructor
        super().__init__()
        #create the sprite's surface with dimentions and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #get the sprite's rect defining defining its position and size
        self.rect = self.image.get_rect()
        #set initioal velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    #methood to update the sprite'spositin
    def update(self):
        #move the sprte by its velocity
        self.rect.move_ip(self.velocity)
        #flag to track if the sprite has hit a boundary
        boundary_hit = False
        #check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        #Chaeck for collsion with top or bottom boundaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        # If ta boundary was hit, post events to change colors
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT)) 
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

            #Method to change the sprite's color
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
        
#Function  to change the background color
def change_background_color(screen):
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

#Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)

sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Boundary Sprite")

bg_color = BLUE

screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color(screen)

    all_sprites_list.update()

    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()