import math
import pygame

class Button:
    def __init__(self, rect, color, text):
        self.rect = rect
        self.color = color
        self.text = text

    def draw(self, surface, font, text_color):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class TextInput:
    def __init__(self, rect, font, color_inactive, color_active, text=''):
        self.rect = rect
        self.font = font
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.color = color_inactive
        self.text = text
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
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
        self.color = self.color_active if self.active else self.color_inactive

    def update(self):
        width = max(140, self.font.size(self.text)[0]+10)
        self.rect.w = width

    def draw(self, surface, text_color):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)  # White background
        pygame.draw.rect(surface, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, text_color)
        surface.blit(text_surface, (self.rect.x+5, self.rect.y+5))
                                                                                                                                                                                                                                                
class Image:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)

    def draw(self, surface, pos):
        surface.blit(self.image, pos)

class Text:
    def __init__(self, text, rect, font, color):
        self.text = text
        self.rect = rect
        self.font = font
        self.color = color

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

class Equilibrio:
    def __init__(self, Menu):
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

        self.text_input = TextInput(pygame.Rect(70, 360, 140, 32), self.font, (173, 216, 230), (30, 144, 255), '50')

        self.img_ten_1 = Image('img/t_1.png')
        self.img_ten_2 = Image('img/t_2.png')
        self.img_bloq = Image('img/p.png')
        
        self.img_ten_1.image = pygame.transform.scale(self.img_ten_1.image, (self.img_ten_1.image.get_width() // 3, self.img_ten_1.image.get_height() // 3))
        self.img_ten_2.image = pygame.transform.scale(self.img_ten_2.image, (self.img_ten_2.image.get_width() // 3, self.img_ten_2.image.get_height() // 3))
        self.img_bloq.image = pygame.transform.scale(self.img_bloq.image, (self.img_bloq.image.get_width() // 3, self.img_bloq.image.get_height() // 3))

        self.text_label = Text('PESO', pygame.Rect(45, 320, 120, 32), self.font, self.black)

        self.increase_button = Button(pygame.Rect(82, 400, 50, 30), (0, 255, 0), '+')
        self.decrease_button = Button(pygame.Rect(150, 400, 50, 30), (255, 0, 0), '-')
        self.result_button = Button(pygame.Rect(70, 450, 130, 40), (0, 0, 0), 'Resultado')
        self.go_to_menu_button = Button(pygame.Rect(70, 830, 60, 40), self.blue_color, 'Regresar')

        self.angulo_t1 = 35
        self.angulo_t2 = 35
        self.tension_1 = 0
        self.tension_2 = 0

        self.running = True

    def resolve_the_situation(self):
        peso_bloque = float(self.text_input.text)
        angulo_t1_rad = math.radians(self.angulo_t1)
        angulo_t2_rad = math.radians(self.angulo_t2)
        self.tension_1 = peso_bloque / (math.sin(angulo_t1_rad) + math.cos(angulo_t1_rad) * math.tan(angulo_t2_rad))
        self.tension_2 = peso_bloque / (math.sin(angulo_t2_rad) + math.cos(angulo_t2_rad) * math.tan(angulo_t1_rad))

    def draw_text(self, surface, text, rect, font, color):
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (rect.x + 5, rect.y + 5))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.text_input.rect.collidepoint(event.pos):
                        self.text_input.active = not self.text_input.active
                    elif self.increase_button.is_clicked(event.pos):
                        self.text_input.text = str(float(self.text_input.text) + 1)
                    elif self.decrease_button.is_clicked(event.pos):
                        self.text_input.text = str(float(self.text_input.text) - 0.5)
                    elif self.result_button.is_clicked(event.pos):
                        self.resolve_the_situation()
                    else:
                        self.text_input.active = False
                elif event.type == pygame.KEYDOWN:
                    if self.text_input.active:
                        if event.key == pygame.K_RETURN:
                            try:
                                self.text_input.text = str(float(self.text_input.text))
                            except ValueError:
                                self.text_input.text = '0'
                            self.text_input.active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.text_input.text = self.text_input.text[:-1]
                        else:
                            self.text_input.text += event.unicode
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
            self.text_input.draw(self.screen, self.black)

            self.text_label.draw(self.screen)

            self.increase_button.draw(self.screen, self.font, self.white)
            self.decrease_button.draw(self.screen, self.font, self.white)
            self.result_button.draw(self.screen, self.font, self.white)
            self.go_to_menu_button.draw(self.screen, self.font, self.white)

            self.text_input.update()

            self.draw_text(self.screen, f'ÁNGULO 1: {self.angulo_t1}', pygame.Rect(45, 220, 200, 32), self.font, self.black)
            self.draw_text(self.screen, f'ÁNGULO 2: {self.angulo_t2}', pygame.Rect(45, 270, 200, 32), self.font, self.black)

            Img_Ten_1_rotate = pygame.transform.rotate(self.img_ten_1.image, -self.angulo_t1)
            Img_Ten_1_rect = Img_Ten_1_rotate.get_rect(center=(550, 320))
            self.screen.blit(Img_Ten_1_rotate, Img_Ten_1_rect)

            Img_Ten_2_rotate = pygame.transform.rotate(self.img_ten_2.image, self.angulo_t2)
            Img_Ten_2_rect = Img_Ten_2_rotate.get_rect(center=(850, 305))
            self.screen.blit(Img_Ten_2_rotate, Img_Ten_2_rect)

            Img_Bloq_rect = self.img_bloq.image.get_rect(center=(710, 540))
            self.screen.blit(self.img_bloq.image, Img_Bloq_rect)

            pygame.draw.rect(self.screen, (self.color_label), pygame.Rect(1130, 563, 255, 200))
            self.draw_text(self.screen, f'Peso = {self.text_input.text}', pygame.Rect(1160, 600, 200, 32), self.font, self.black)
            self.draw_text(self.screen, f'Tensión 1 = {self.tension_1:.2f}', pygame.Rect(1160, 650, 200, 32), self.font, self.black)
            self.draw_text(self.screen, f'Tensión 2 = {self.tension_2:.2f}', pygame.Rect(1160, 700, 200, 32), self.font, self.black)

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    import menu
    menu_instance = menu.Menu()
    equilibrio = Equilibrio(menu_instance)
    equilibrio.run()