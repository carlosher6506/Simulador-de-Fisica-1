import math
import pygame
import subprocess

angulo_t1 = 35
angulo_t2 = 35
tension_1 = 0
tension_2 = 0
# Function that solves the exercises
def resolve_the_situation(angulo_t1, angulo_t2):
    global tension_1, tension_2
    peso_bloque = float(text)
    angulo_t1_rad = math.radians(angulo_t1) 
    angulo_t2_rad = math.radians(angulo_t2) 
    tension_1 = peso_bloque / (math.sin( angulo_t1_rad) + math.cos(angulo_t1_rad) * math.tan(angulo_t2_rad))
    tension_2 = peso_bloque / (math.sin(angulo_t2_rad) + math.cos(angulo_t2_rad) * math.tan(angulo_t1_rad))

# Function that draws the text next to the text input
def draw_text(surface, text, rect, font, color):
    text_surface = font.render(text, True, color)
    width = max(rect.width, text_surface.get_width() + 10)
    rect.width = width
    surface.blit(text_surface, (rect.x + 5, rect.y + 5))
    
def ir_menu():
    ruta_ventana = "Menu.py" 
    subprocess.Popen(["python", ruta_ventana])
    screen.destroy() 

pygame.init()

# Window Size
width = 1350
height = 840
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption('Equilibrio Estatico')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
blue_color = (0, 71, 125)
color_label = (226,220,198)
font = pygame.font.Font(None, 34)

# Text Input Box
input_1 = pygame.Rect(70, 360, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = '50'

# Loading Image
Img_Ten_1 = pygame.image.load('img/t_1.png')
Img_Ten_2 = pygame.image.load('img/t_2.png')
Img_Bloq = pygame.image.load('img/p.png')

# Size Image
nuevo_ancho = Img_Ten_1.get_width() // 3
nuevo_alto = Img_Ten_1.get_height() // 3
Img_Ten_1 = pygame.transform.scale(Img_Ten_1, (nuevo_ancho, nuevo_alto))

nuevo_ancho2 = Img_Ten_2.get_width() // 3
nuevo_alto2 = Img_Ten_2.get_height() // 3
Img_Ten_2 = pygame.transform.scale(Img_Ten_2, (nuevo_ancho2, nuevo_alto2))

nuevo_ancho3 = Img_Bloq.get_width() // 3  
nuevo_alto3 = Img_Bloq.get_height() // 3
Img_Bloq = pygame.transform.scale(Img_Bloq, (nuevo_ancho3, nuevo_alto3))

# Texto junto a la entrada de texto 
text_label = 'PESO'

# Botones de incremento y decremento
increase_button_rect = pygame.Rect(82, 400, 50, 30)
decrease_button_rect = pygame.Rect(150, 400, 50, 30)
increase_button_color = pygame.Color('green')
decrease_button_color = pygame.Color('red')

#button for resove function
btn_function = pygame.Rect(350, 100, 50, 30)
btn_function_color = pygame.Color('black')

btn_go_to_menu = pygame.Rect(70, 830, 60, 40)
btn_go_to_menu_color = pygame.Color(blue_color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if input_1.collidepoint(event.pos):
                active = not active
            elif increase_button_rect.collidepoint(event.pos):
                text = str(float(text) + 1)
            elif decrease_button_rect.collidepoint(event.pos):
                text = str(float(text) - 0.5)
            elif btn_function.collidepoint(event.pos):
                resolve_the_situation(angulo_t1, angulo_t2)
            elif btn_function.collidepoint(event.pos):
                resolve_the_situation(angulo_t1, angulo_t2)
            elif btn_go_to_menu.collidepoint(event.pos):
                ir_menu()
            else:
                active = False
            color = color_active if active else color_inactive
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    try:
                        text = str(float(text))
                    except ValueError:
                        text = '0'
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.key == pygame.K_LEFT:
                angulo_t1 -= 1
            if event.key == pygame.K_RIGHT:
                angulo_t1 += 1
            if event.key == pygame.K_1:
                angulo_t2 -= 1
            if event.key == pygame.K_2:
                angulo_t2 += 1
                    
    screen.fill(white)
    pygame.draw.rect(screen, blue_color, (0, 0, 1440, 45))
    pygame.draw.rect(screen, blue_color, (0, 820, 1440, 60))
                
    if angulo_t1 > 90:
        angulo_t1 = 90
    elif angulo_t1 < -90:
        angulo_t1 = -90
    
    if angulo_t2 > 90:
        angulo_t2 = 90
    elif angulo_t2 < -90:
        angulo_t2 = -90
        
    pygame.draw.rect(screen, (color_label), pygame.Rect(28, 200, 220, 315))
    pygame.draw.rect(screen, (white), pygame.Rect(183, 220, 35, 35))
    pygame.draw.rect(screen, (white), pygame.Rect(183, 270, 35, 35))
    pygame.draw.rect(screen, (white), pygame.Rect(70, 360, 140, 32))
        
    draw_text(screen, f'ÁNGULO 1: {angulo_t1}', pygame.Rect(45, 220, 200, 32), font, black)
    draw_text(screen, f'ÁNGULO 2: {angulo_t2}', pygame.Rect(45, 270, 200, 32), font, black)
        
    # Dibujar el texto junto a la entrada de texto
    draw_text(screen, text_label, pygame.Rect(45, 320, 120, 32),font, black)
    
    # Dibujar el cuadro de entrada de texto
    pygame.draw.rect(screen, color, input_1, 2)
    draw_text(screen, text, input_1,font, color)

    # draw the button of increment and decrement
    pygame.draw.rect(screen, increase_button_color, increase_button_rect)
    pygame.draw.rect(screen, decrease_button_color, decrease_button_rect)

    # Text in the button
    draw_text(screen, "+", increase_button_rect,font, white)
    draw_text(screen, "-", decrease_button_rect,font, white)

    #draw button function
    btn_function = pygame.Rect(70, 450, 130, 40)
    pygame.draw.rect(screen, btn_function_color, btn_function)
    draw_text(screen, 'Resultado', btn_function, font, white)
        
    pygame.draw.rect(screen, (color_label), pygame.Rect(1130, 563, 255, 200))
    draw_text(screen, f'Peso = {text}', pygame.Rect(1160, 600, 200, 32), font, black)
    draw_text(screen, f'Tensión 1 = {tension_1:.2f}', pygame.Rect(1160, 650, 200, 32), font, black)
    draw_text(screen, f'Tensión 2 = {tension_2:.2f}', pygame.Rect(1160, 700, 200, 32), font, black)
    
    pygame.draw.rect(screen, btn_go_to_menu_color, btn_go_to_menu)
    draw_text(screen, '<-- Regresar', btn_go_to_menu, font, white)

    Img_Ten_1_rotate = pygame.transform.rotate(Img_Ten_1, -angulo_t1)
    Img_Ten_1_rect = Img_Ten_1_rotate.get_rect(center=(550,320))
    screen.blit(Img_Ten_1_rotate, Img_Ten_1_rect)
        
    Img_Ten_2_rotate = pygame. transform.rotate(Img_Ten_2, angulo_t2)
    Img_Ten_2_rect = Img_Ten_2_rotate.get_rect(center=(850,305))
    screen.blit(Img_Ten_2_rotate, Img_Ten_2_rect)
        
    Img_Bloq_rect = Img_Bloq.get_rect(center=(710, 540))
    screen.blit(Img_Bloq, Img_Bloq_rect)

    pygame.display.flip()

pygame.quit()