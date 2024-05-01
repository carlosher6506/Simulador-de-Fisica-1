import pygame
import subprocess

def ir_tiro():
    ruta_ventana = "Routes.py" 
    subprocess.Popen(["python", ruta_ventana])
    screen.destroy() 
    
def ir_cuerpo():
    ruta_ventana = "pages/Cuerpos_Equilibrio.py" 
    subprocess.Popen(["python", ruta_ventana])
    screen.destroy()     

pygame.init()

width = 1350
height = 840
screen = pygame.display.set_mode((width,height ), pygame.RESIZABLE)
pygame.display.set_caption('PHYSICS SIMULATOR DEV-9')

# Colores
bg_color = (0, 0, 25)
blue_color = (0, 71, 125)
white_color = (255, 255, 255)
    
imagen = pygame.image.load("img/fondo.png")
imagen1 = pygame.transform.scale(imagen, (400, 300))
imagen_1 = pygame.image.load("img/ten.png")
imagen2 = pygame.transform.scale(imagen_1, (400, 308))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_proyectile.collidepoint(event.pos):
                ir_tiro()
                running = False
            elif btn_estatic.collidepoint(event.pos):
                ir_cuerpo()
                running = False

    # Dibujar elementos en la pantalla
    screen.fill(bg_color)
    pygame.draw.rect(screen, blue_color, (0, 0, 1440, 45))

    #Letras de la interfaz
    font = pygame.font.Font(None, 56)
    title_text = font.render('PHYSICS', True, white_color)
    screen.blit(title_text, (615, 350))
    title_text2 = font.render('SIMULATOR', True, white_color)
    screen.blit(title_text2, (589, 405))
    title_text3 = font.render('DEV-9', True, white_color)
    screen.blit(title_text3, (645, 460))

    #Boton para ir al tiro parabolico
    font = pygame.font.Font(None, 24)
    btn_proyectile = pygame.draw.rect(screen, blue_color, (200, 625, 170, 35))
    btn_proyectile_text = font.render('Tiro Parabólico', True, white_color)
    screen.blit(btn_proyectile_text, (225, 635))

    #boton para ir a cuerpos en equilibrio
    btn_estatic = pygame.draw.rect(screen, blue_color, (1050, 625, 170, 35))
    btn_estatic_text = font.render('Equilibrio Estatico', True, white_color)
    screen.blit(btn_estatic_text, (1065, 635))

    #imagenes de las interfaces
    screen.blit(imagen1, (100, 300))
    screen.blit(imagen2, (930, 300))

    pygame.display.flip()

# Salir de Pygame
pygame.quit()