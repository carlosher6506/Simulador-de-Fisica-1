import pygame
from pages.Bodies_in_balance.bodies import Equilibrio


class Menu:
    def __init__(self):
        pygame.init()
        
        self.width = 1350
        self.height = 840
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('JC SIMULATOR')
        
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 71, 125)
        self.font = pygame.font.Font(None, 34)
        
        self.options = [
            ('Tiro Parabolico', (self.width // 2, 150)),
            ('Equilibrio Estatico', (self.width // 2, 200)),
            ('Evaluar', (self.width // 2, 250)),
            ('Opciones', (self.width // 2, 300)),
            ('Salir', (self.width // 2, 350))
        ]
        
        self.runing = True
        
    def draw_text(self, surface, text, pos, font, color):
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, pos)
        
    def run(self):
        while self.runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, (text, pos) in enumerate (self.options):
                        rect = pygame.Rect(pos [0] - 100, pos[1] - 20, 200, 40)
                        if rect.collidepoint(event.pos):
                            if text == "Equilibrio Estatico":
                                equilibrio = Equilibrio(self)
                                equilibrio.run()
                                self.runing = False
                                
            self.screen.fill(self.white)
            pygame.draw.rect(self.screen, self.blue, (0, 0, self.width, self.height))
            
            for text, pos in self.options:
                self.draw_text(self.screen, text, pos, self.font, self.black)
                
            pygame.display.flip()
            
        pygame.quit()
        
if __name__ == "__main__":
    menu = Menu()
    menu.run()