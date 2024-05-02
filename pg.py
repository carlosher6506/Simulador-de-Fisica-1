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
    xPositions, yPositions = [], []
    for t in intervals:
        xPositions.append(18 * (u * math.cos(theta) * t))
        yPositions.append(18 * (u * math.sin(theta) * t - 0.5 * gravity * t * t))
    return xPositions, yPositions

def calculate_angle(pivot, pos):
    """Calculate the angle between the horizontal and the line joining the pivot and pos."""
    dx = pos[0] - pivot[0]
    dy = pivot[1] - pos[1]  # Invert dy due to Pygame's y-coordinate being downwards.
    if dx == 0:
        dx = 0.01  # Prevent division by zero
    angle = math.degrees(math.atan(dy / dx))
    return angle + 90 if dx > 0 else angle + 270

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_size):
        super().__init__()
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect(topleft=(0, 0))

    def update_image(self, screen_size):
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect(topleft=(0, 0))

class Slider:
    def __init__(self, x, y, w, h, min, max, step, initial_value, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.min = min
        self.max = max
        self.step = step
        self.value = initial_value
        self.knob = pygame.Rect(x, y, 20, h)
        self.knob.centerx = x + (initial_value - min) / (max - min) * w
        self.font = font

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        pygame.draw.rect(surface, (100, 100, 250), self.knob)
        val_text = self.font.render(f"Rapidez Inicial {int(self.value)} m/s", True, (0, 0, 0))
        surface.blit(val_text, (self.rect.centerx, self.rect.centery - 40))

    def move_knob(self, pos):
        if self.rect.collidepoint(pos):
            self.knob.centerx = max(min(pos[0], self.rect.right), self.rect.left)
            self.value = (self.knob.centerx - self.rect.x) / self.rect.width * (self.max - self.min) + self.min

class ProjectileSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, initial_position):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=initial_position)

    def update_position(self, new_position):
        """Update the position of the projectile."""
        self.rect.center = new_position

class CannonSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (100, 50))
        self.rect = self.image.get_rect(midbottom=(x, y))

pygame.init()
width, height = 1124, 860
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
coordinatesFont = pygame.font.SysFont("Comic Sans MS", 20)

background = BackgroundSprite("./img/fondo.png", (width, height))
slider = Slider(350, 700, 300, 20, 0, 30, 1, 15, coordinatesFont)
button = pygame.Rect(100, 700, 200, 50)
velocity = slider.value
angle = 45
gravity = 9.8
x, y = draw_trajectory(velocity, angle, gravity)
projectile = ProjectileSprite("./img/pelota.png", (x[0], height - y[0]))
cannon = CannonSprite("./img/c_ca.png", 48, 870)

clock = pygame.time.Clock()
simulate = False
dragging = False
current_index = 0
trajectory_points = []  # Lista para almacenar puntos de la trayectoria
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background.update_image((event.w, event.h))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if slider.knob.collidepoint(event.pos):
                dragging = True
            elif button.collidepoint(event.pos):
                simulate = True
                current_index = 0
                x, y = draw_trajectory(velocity, angle, gravity)
                trajectory_points = []  # Reiniciar puntos de trayectoria
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            slider.move_knob(event.pos)
            velocity = slider.value

    screen.blit(background.image, background.rect)
    slider.draw(screen)
    pygame.draw.rect(screen, (0, 255, 0), button)
    buttonText = coordinatesFont.render("Start Simulation", True, (0, 0, 0))
    screen.blit(buttonText, (button.x + 50, button.y + 15))
    screen.blit(cannon.image, cannon.rect)

    for point in trajectory_points:
        pygame.draw.circle(screen, (0, 0, 255), point, 3)  # Dibuja el rastro

    if simulate and current_index < len(x):
        projectile.update_position((x[current_index], height - y[current_index]))
        trajectory_points.append((x[current_index], height - y[current_index]))
        screen.blit(projectile.image, projectile.rect)
        current_index += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

###