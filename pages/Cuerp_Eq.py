import math
import pygame

class Equilibrio:
    def __init__(self):
        pygame.init()

        self.width = 1350
        self.height = 840
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Equilibrio Estatico')

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue_color = (0, 71, 125)
        self.color_label = (226, 220, 198)
        self.font = pygame.font.Font(None, 34)

        self.input_1 = pygame.Rect(70, 360, 140, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = '50'

        self.Img_Ten_1 = pygame.image.load('img/t_1.png')
        self.Img_Ten_2 = pygame.image.load('img/t_2.png')
        self.Img_Bloq = pygame.image.load('img/p.png')

        self.nuevo_ancho = self.Img_Ten_1.get_width() // 3
        self.nuevo_alto = self.Img_Ten_1.get_height() // 3
        self.Img_Ten_1 = pygame.transform.scale(self.Img_Ten_1, (self.nuevo_ancho, self.nuevo_alto))

        self.nuevo_ancho2 = self.Img_Ten_2.get_width() // 3
        self.nuevo_alto2 = self.Img_Ten_2.get_height() // 3
        self.Img_Ten_2 = pygame.transform.scale(self.Img_Ten_2, (self.nuevo_ancho2, self.nuevo_alto2))

        self.nuevo_ancho3 = self.Img_Bloq.get_width() // 3
        self.nuevo_alto3 = self.Img_Bloq.get_height() // 3
        self.Img_Bloq = pygame.transform.scale(self.Img_Bloq, (self.nuevo_ancho3, self.nuevo_alto3))

        self.text_label = 'PESO'

        self.increase_button_rect = pygame.Rect(82, 400, 50, 30)
        self.decrease_button_rect = pygame.Rect(150, 400, 50, 30)
        self.increase_button_color = pygame.Color('green')
        self.decrease_button_color = pygame.Color('red')

        self.btn_function = pygame.Rect(350, 100, 50, 30)
        self.btn_function_color = pygame.Color('black')

        self.btn_go_to_menu = pygame.Rect(70, 830, 60, 40)
        self.btn_go_to_menu_color = pygame.Color(self.blue_color)

        self.angulo_t1 = 35
        self.angulo_t2 = 35
        self.tension_1 = 0
        self.tension_2 = 0

        self.running = True

    def resolve_the_situation(self):
        peso_bloque = float(self.text)
        angulo_t1_rad = math.radians(self.angulo_t1)
        angulo_t2_rad = math.radians(self.angulo_t2)
        self.tension_1 = peso_bloque / (math.sin(angulo_t1_rad) + math.cos(angulo_t1_rad) * math.tan(angulo_t2_rad))
        self.tension_2 = peso_bloque / (math.sin(angulo_t2_rad) + math.cos(angulo_t2_rad) * math.tan(angulo_t1_rad))

    def draw_text(self, surface, text, rect, font, color):
        text_surface = font.render(text, True, color)
        width = max(rect.width, text_surface.get_width() + 10)
        rect.width = width
        surface.blit(text_surface, (rect.x + 5, rect.y + 5))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_1.collidepoint(event.pos):
                        self.active = not self.active
                    elif self.increase_button_rect.collidepoint(event.pos):
                        self.text = str(float(self.text) + 1)
                    elif self.decrease_button_rect.collidepoint(event.pos):
                        self.text = str(float(self.text) - 0.5)
                    elif btn_function.collidepoint(event.pos):
                        self.resolve_the_situation()
                    elif self.btn_go_to_menu.collidepoint(event.pos):
                        self.ir_menu()
                    else:
                        self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                elif event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            try:
                                self.text = str(float(self.text))
                            except ValueError:
                                self.text = '0'
                            self.active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
                    if event.key == pygame.K_LEFT:
                        self.angulo_t1 -= 1
                    if event.key == pygame.K_RIGHT:
                        self.angulo_t1 += 1
                    if event.key == pygame.K_1:
                        self.angulo_t2 -= 1
                    if event.key == pygame.K_2:
                        self.angulo_t2 += 1

            self.screen.fill(self.white)
            pygame.draw.rect(self.screen, self.blue_color, (0, 0, 1440, 45))
            pygame.draw.rect(self.screen, self.blue_color, (0, 820, 1440, 60))

            if self.angulo_t1 > 90:
                self.angulo_t1 = 90
            elif self.angulo_t1 < -90:
                self.angulo_t1 = -90

            if self.angulo_t2 > 90:
                self.angulo_t2 = 90
            elif self.angulo_t2 < -90:
                self.angulo_t2 = -90

            pygame.draw.rect(self.screen, (self.color_label), pygame.Rect(28, 200, 220, 315))
            pygame.draw.rect(self.screen, (self.white), pygame.Rect(183, 220, 35, 35))
            pygame.draw.rect(self.screen, (self.white), pygame.Rect(183, 270, 35, 35))
            pygame.draw.rect(self.screen, (self.white), pygame.Rect(70, 360, 140, 32))

            self.draw_text(self.screen, f'ÁNGULO 1: {self.angulo_t1}', pygame.Rect(45, 220, 200, 32), self.font, self.black)
            self.draw_text(self.screen, f'ÁNGULO 2: {self.angulo_t2}', pygame.Rect(45, 270, 200, 32), self.font, self.black)

            self.draw_text(self.screen, self.text_label, pygame.Rect(45, 320, 120, 32), self.font, self.black)

            pygame.draw.rect(self.screen, self.color, self.input_1, 2)
            self.draw_text(self.screen, self.text, self.input_1, self.font, self.color)

            pygame.draw.rect(self.screen, self.increase_button_color, self.increase_button_rect)
            pygame.draw.rect(self.screen, self.decrease_button_color, self.decrease_button_rect)

            self.draw_text(self.screen, "+", self.increase_button_rect, self.font, self.white)
            self.draw_text(self.screen, "-", self.decrease_button_rect, self.font, self.white)

            btn_function = pygame.Rect(70, 450, 130, 40)
            pygame.draw.rect(self.screen, self.btn_function_color, btn_function)
            self.draw_text(self.screen, 'Resultado', btn_function, self.font, self.white)

            pygame.draw.rect(self.screen, (self.color_label), pygame.Rect(1130, 563, 255, 200))
            self.draw_text(self.screen, f'Peso = {self.text}', pygame.Rect(1160, 600, 200, 32), self.font, self.black)
            self.draw_text(self.screen, f'Tensión 1 = {self.tension_1:.2f}', pygame.Rect(1160, 650, 200, 32), self.font, self.black)
            self.draw_text(self.screen, f'Tensión 2 = {self.tension_2:.2f}', pygame.Rect(1160, 700, 200, 32), self.font, self.black)

            pygame.draw.rect(self.screen, self.btn_go_to_menu_color, self.btn_go_to_menu)
            self.draw_text(self.screen, '<-- Regresar', self.btn_go_to_menu, self.font, self.white)

            Img_Ten_1_rotate = pygame.transform.rotate(self.Img_Ten_1, -self.angulo_t1)
            Img_Ten_1_rect = Img_Ten_1_rotate.get_rect(center=(550, 320))
            self.screen.blit(Img_Ten_1_rotate, Img_Ten_1_rect)

            Img_Ten_2_rotate = pygame.transform.rotate(self.Img_Ten_2, self.angulo_t2)
            Img_Ten_2_rect = Img_Ten_2_rotate.get_rect(center=(850, 305))
            self.screen.blit(Img_Ten_2_rotate, Img_Ten_2_rect)

            Img_Bloq_rect = self.Img_Bloq.get_rect(center=(710, 540))
            self.screen.blit(self.Img_Bloq, Img_Bloq_rect)

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    equilibrio = Equilibrio()
    equilibrio.run()