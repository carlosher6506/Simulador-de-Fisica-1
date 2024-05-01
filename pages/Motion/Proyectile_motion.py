import pygame
import math

class Proyectile:
    def __init__(self):
        pygame.init()
        
        #Window dimensions and settings
        self.width = 1024
        self.height = 840
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Lanzamiento De Un Proyectil')
        self.textSurface = pygame.Surface((350, 80))
        
        #Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 71, 125)
        self.color_label = (226, 220, 198)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.increase_button_color = pygame.Color('green')
        self.decrease_button_color = pygame.Color('red')
        
        #Text font and angle
        self.angle = 45
        self.font = pygame.font.Font(None, 34)
        
        #Loading images
        self.img_background = pygame.image.load('img/fondo.png')
        self.img_cannon_base = pygame.image.load('img/b_ca.png')
        self.img_barrel_body = pygame.image.load('img/c_ca.png')
        self.img_ball = pygame.image.load('img/pelota.png')
        self.img_top = pygame.image.load('img/ t_ca.png')
        
        #Image resizing
        self.new_width = self.img_cannon_base.get_width() // 2
        self.new_height = self.img_cannon_base.get_height() // 2
        self.image_1 = pygame.transform.scale(self.img_cannon_base, (self.new_width, self.new_height))
        
        self.new_width = self.img_barrel_body.get_width() // 2
        self.new_height = self.img_barrel_body.get_height() // 2
        self.image_2 = pygame.transform.scale(self.img_barrel_body, (self.new_width, self.new_height))

        self.new_width = self.img_ball.get_width() // 40
        self.new_height = self.img_ball.get_height() // 40
        self.image_3 = pygame.transform.scale(self.img_ball, (self.new_width, self.new_height))
        
        self.new_width = self.img_top.get_width() // 2
        self.new_height = self.img_top.get_height() // 2
        self.image_4 = pygame.transform.scale(self.img_top, (self.new_width, self.new_height))
        
        #Data entry
        self.input_1 = pygame.Rect(80, 97, 140, 32)
        self.color = self.color_inactive
        self.active = False
        self.velocity = '90'

        self.input_2 = pygame.Rect(80, 210, 140, 32)
        self.color_2 = self.color_active
        self.active_2 = False
        self.gravity = '9.8'
        
        self.clock = pygame.time.Clock()
        
        #Arrays and variables globals
        self.x = []
        self.y = []
        global time_of_flight, max_height, projectile_range

        #Text next to text entry
        self.text_velocity = 'Velocidad Inicial'
        self.text_gavity = 'Gravedad'

        #Increment and decrement buttons
        self.increase_button_rect = pygame.Rect(100, 135, 50, 30)
        self.decrease_button_rect = pygame.Rect(150, 135, 50, 30)

        #Buttons for operation
        self.execution_button = pygame.Rect(100, 840, 50, 30)
        self.execution_button = pygame.Color(self.white)

        self.btn_result = pygame.Rect(220,840,50,30)
        self.btn_result_color = pygame.Color(self.white)

        self.btn_go_to_menu = pygame.Rect(365, 840, 60, 40)
        self.btn_go_to_menu_color = pygame.Color(self.blue)

        #Variables for trajectory and results
        self.historial_puntos = []
        self.draw_trajectory_flag = False
        self.show_results_flag = False
        
        self.runing = True
        
    def run (self):
        while self.runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_1.collidepoint(event.pos):
                        self.active = not self.active
                    elif self.input_2.collidepoint(event.pos):
                        self.active_2 = not self.active_2
                    elif increase_button_rect.collidepoint(event.pos):
                        if self.active:
                            self.velocity = str(float(self.velocity) + 1)
                        elif self.active_2:
                            self.gravity = str(float(self.gravity) + 1) 