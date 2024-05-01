import math
import pygame

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers

def draw_trajectory(u, theta, gravity):
    theta = math.radians(theta)
    t_flight = 2 * u * math.sin(theta) / gravity
    intervals = frange(0, t_flight, 0.020)
    
    xPositions = []
    yPositions = []
    for t in intervals:
        xPositions.append(u * math.cos(theta) * t)
        yPositions.append(u * math.sin(theta) * t - 0.5 * gravity * t * t)
    return xPositions, yPositions

def coordinatesText(surf, xCord, yCord, font):
    labelX = font.render("X coordinate: " + str(xCord), True, (255, 0, 0))
    labelY = font.render("Y coordinate: " + str(yCord), True, (255, 0, 0))
    surf.fill((0, 0, 0))  # Clear previous text
    surf.blit(labelX, (10, 10))
    surf.blit(labelY, (10, 40))

class Slider:
    def __init__(self, x, y, w, h, min, max, step, initial_value, font):
        self.rect = pygame.Rect(x, y, w, h)  # Base rectangle for slider
        self.min = min
        self.max = max
        self.step = step
        self.value = initial_value
        self.knob = pygame.Rect(x, y, 20, h)  # Slider knob
        self.knob.centerx = x + (initial_value - min) / (max - min) * w
        self.font = font  # Font for displaying the value

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)  # Slider background
        pygame.draw.rect(surface, (100, 100, 250), self.knob)  # Slider knob
        val_text = self.font.render(f"Rapidez Inicial {int(self.value)} m/s", True, (0, 0, 0))
        text_rect = val_text.get_rect(center=(self.rect.centerx, self.rect.centery - 40))
        surface.blit(val_text, text_rect)  # Display the current value above the slider

    def move_knob(self, pos):
        if self.rect.collidepoint(pos):
            self.knob.centerx = max(min(pos[0], self.rect.right), self.rect.left)
            self.value = (self.knob.centerx - self.rect.x) / self.rect.width * (self.max - self.min) + self.min

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_size):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect(topleft=(0, 0))

class ProjectileSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, initial_position, size=(30, 30)):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=initial_position)

    def update_position(self, new_position):
        self.rect.center = new_position

pygame.init()

width = 1024
height = 800
FPS = 60

screen = pygame.display.set_mode((width, height))
coordinatesFont = pygame.font.SysFont("Comic Sans MS", 20)
textSurface = pygame.Surface((350, 80))

# Slider and button initialization
slider = Slider(350, 700, 300, 20, 0, 30, 1, 15, coordinatesFont)
button = pygame.Rect(100, 700, 200, 50)  # Button coordinates

clock
