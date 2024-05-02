import pygame
import math
import subprocess

def ir_menu():
    ruta_ventana = "Menu.py" 
    subprocess.Popen(["python", ruta_ventana])
    screen.destroy() 
    
# Function that draws the text next to the text input
def draw_text(surface, text, rect, font, color):
    text_surface = font.render(text, True, color)
    width = max(rect.width, text_surface.get_width() + 10)
    rect.width = width
    surface.blit(text_surface, (rect.x + 5, rect.y + 5))

def resize_image(image, window_size):
        return pygame.transform.scale(image, window_size)
    
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment 
    return numbers


# Aumenta el tiempo de vuelo en draw_trajectory
def draw_trajectory(u, theta, gravity, xPositions=[], yPositions=[], initial_position=(50, 179)):
    theta = math.radians(theta)
    u_multiplied = u * 5  # Velocidad multiplicada por 5 para la animación
    t_flight = 2 * u_multiplied * math.sin(theta) / gravity  
    t_extended = t_flight * 1.5  # Extiende el tiempo de vuelo para permitir que la pelota siga cayendo
    intervals = frange(0.12, t_extended, 0.013)
    for t in intervals:
        x_pos = initial_position[0] + u_multiplied * math.cos(theta) * t
        y_pos = initial_position[1] + u_multiplied * math.sin(theta) * t - 0.5 * gravity * t * t
        xPositions.append(x_pos)
        yPositions.append(y_pos)  # No limites y aquí
    return xPositions, yPositions


pygame.init()

width = 1024
height = 840
FPS = 120
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Lanzamiento De Un Proyectil')
textSurface = pygame.Surface((350, 80))

angle = 45

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
blue_color = (0, 71, 125)
color_label = (226,220,198)
font = pygame.font.Font(None, 34)

imag = pygame.image.load('img/fondo.png')
imagen_base_canon = pygame.image.load('img/b_ca.png')
imagen_cuerpo_canon = pygame.image.load('img/c_ca.png')
imagen_pelota = pygame.image.load('img/pelota.png')
imagen_tapa = pygame.image.load('img/t_ca.png')

nuevo_ancho = imagen_base_canon.get_width() // 2
nuevo_alto = imagen_base_canon.get_height() // 2
imagen_1 = pygame.transform.scale(imagen_base_canon, (nuevo_ancho, nuevo_alto))
nuevo_ancho = imagen_cuerpo_canon.get_width() // 2
nuevo_alto = imagen_cuerpo_canon.get_height() // 2
imagen_2 = pygame.transform.scale(imagen_cuerpo_canon, (nuevo_ancho, nuevo_alto))
nuevo_ancho = imagen_pelota.get_width() // 50
nuevo_alto = imagen_pelota.get_height() // 50
imagen_3 = pygame.transform.scale(imagen_pelota, (nuevo_ancho, nuevo_alto))
nuevo_ancho = imagen_tapa.get_width() // 2
nuevo_alto = imagen_tapa.get_height() // 2
imagen_4 = pygame.transform.scale(imagen_tapa, (nuevo_ancho, nuevo_alto))

cannon_body_rect = imagen_2.get_rect()
cannon_body_width = cannon_body_rect.width
cannon_body_height = cannon_body_rect.height

ball_rect = imagen_3.get_rect()
ball_radius = ball_rect.width // 2

input_1 = pygame.Rect(80, 97, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
velocity = '20'

input_2 = pygame.Rect(80, 210, 140, 32)
color_inactive_2 = pygame.Color('lightskyblue3')
color_active_2 = pygame.Color('dodgerblue2')
color_2 = color_active_2
active_2 = False
gravity = '9.8'

clock = pygame.time.Clock()
x = []
y = []
global time_of_flight, max_height, projectile_range

# Texto junto a la entrada de texto 
text_label = 'Velocidad Inicial'
text_label_2 = 'Gravedad'

# Botones de incremento y decremento
increase_button_rect = pygame.Rect(100, 135, 50, 30)
decrease_button_rect = pygame.Rect(150, 135, 50, 30)
increase_button_color = pygame.Color('green')
decrease_button_color = pygame.Color('red')


#button for resove function
btn_function = pygame.Rect(100, 840, 50, 30)
btn_function_color = pygame.Color(white)

btn_result = pygame.Rect(220,840,50,30)
btn_result_color = pygame.Color(white)

btn_go_to_menu = pygame.Rect(365, 840, 60, 40)
btn_go_to_menu_color = pygame.Color(blue_color)

historial_puntos = []
draw_trajectory_flag = False
show_results_flag = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if btn_function.collidepoint(event.pos):
                x = []
                y = []
                historial_puntos = []
                draw_trajectory_flag = True
            if input_1.collidepoint(event.pos):
                active = not active
            elif input_2.collidepoint(event.pos):
                active_2 = not active_2
            elif increase_button_rect.collidepoint(event.pos):
                if active:
                    velocity = str(float(velocity) + 1)
                elif active_2:
                    gravity = str(float(gravity) + 1)
            elif decrease_button_rect.collidepoint(event.pos):
                if active:
                    velocity = str(float(velocity) - 0.5)
                elif active_2:
                    gravity = str(float(gravity) - 0.5)
            elif btn_result.collidepoint(event.pos):
                show_results_flag = True
            elif btn_go_to_menu.collidepoint(event.pos):
                ir_menu()
            else:
                active = False
                active_2 = False
            color = color_active if active else color_inactive
            color_2 = color_active_2 if active_2 else color_inactive_2
        elif event.type == pygame.KEYUP:
            if active:
                if event.key == pygame.K_RETURN:
                    try:
                        velocity = str(float(velocity))
                    except ValueError:
                        velocity = '0'
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    velocity = velocity[:-1]
                else:
                    velocity += event.unicode
            if active_2:
                if event.key == pygame.K_RETURN:
                    try:
                        gravity = str(float(gravity))
                    except ValueError:
                        gravity = '0'
                    active_2 = False
                elif event.key == pygame.K_BACKSPACE:
                    gravity = gravity[:-1]
                else:
                    gravity += event.unicode
            if event.key == pygame.K_LEFT:
                angle -= 5
            if event.key == pygame.K_RIGHT:
                angle += 5
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            imag = resize_image(imag, (width, height))
                
    screen.blit(imag,(0,0))
    pygame.draw.rect(screen, blue_color, (0, 0, 1440, 35))
    pygame.draw.rect(screen, blue_color, (0, 833, 1440, 52))
    
    if angle > 90:
        angle = 90
    elif angle < -90:
        angle = -90
    
    #Label the font of entry text
    pygame.draw.rect(screen, (color_label), pygame.Rect(26, 50, 250, 230))
    pygame.draw.rect(screen, (white), pygame.Rect(80, 97, 140, 32))
    pygame.draw.rect(screen, (white), pygame.Rect(80, 210, 140, 32))
    
    # Dibujar el texto junto a la entrada de texto
    draw_text(screen, text_label, pygame.Rect(50, 60, 120, 32),font, black)
    
    # Dibujar el cuadro de entrada de texto
    pygame.draw.rect(screen, color, input_1, 2)
    draw_text(screen, velocity, input_1,font, color)

    # draw the button of increment and decrement
    pygame.draw.rect(screen, increase_button_color, increase_button_rect)
    pygame.draw.rect(screen, decrease_button_color, decrease_button_rect)
    draw_text(screen, "+", increase_button_rect,font, white)
    draw_text(screen, "-", decrease_button_rect,font, white)
    
    draw_text(screen, text_label_2, pygame.Rect(90,175,120,32),font, black)
    pygame.draw.rect(screen, color_2,input_2,2 )
    draw_text(screen, gravity, input_2, font, color_2)
    
    if draw_trajectory_flag:
        time_of_flight, max_height, projectile_range, original_t_flight, original_max_height, original_projectile_range, original_velocity = draw_trajectory(float(velocity), float(angle), float(gravity), x, y)
        draw_trajectory_flag = False  
        
        
    if show_results_flag:
        pygame.draw.rect(screen, (color_label), pygame.Rect(1120, 50, 300, 280))
        pygame.draw.rect(screen, (white), pygame.Rect(1227, 80, 110, 32))
        draw_text(screen, f'Tiempo Original: {original_t_flight:.2f}', pygame.Rect(1130, 180, 220, 32), font, black)  # Mostrar el tiempo original
        pygame.draw.rect(screen, (white), pygame.Rect(1227, 120, 110, 32))
        draw_text(screen, f'Altura Max. Original: {original_max_height:.2f}', pygame.Rect(1130, 200, 200, 32), font, black)  # Mostrar la altura máxima original
        pygame.draw.rect(screen, (white), pygame.Rect(1218, 240, 110, 32))
        draw_text(screen, f'Rango Original: {original_projectile_range:.2f}', pygame.Rect(1130, 280, 200, 32), font, black)  # Mostrar el rango original
        pygame.draw.rect(screen, (white), pygame.Rect(1218, 320, 110, 32))
        draw_text(screen, f'Velocidad: {original_velocity}', pygame.Rect(1130, 320, 200, 32), font, black)  # Mostrar la velocidad original
    
    pygame.draw.rect(screen, btn_function_color, btn_function)
    draw_text(screen, 'Ejecutar', btn_function, font, black)
    
    pygame.draw.rect(screen, btn_result_color, btn_result)
    draw_text(screen, 'Resultados', btn_result, font, black)
    
    pygame.draw.rect(screen, btn_go_to_menu_color, btn_go_to_menu)
    draw_text(screen, '<-- Regresar', btn_go_to_menu, font, white)
    
    #Base del cañon
    base_rect = imagen_1.get_rect(center=(50,800))
    screen.blit(imagen_1, base_rect.topleft)
    
    #Base del cañon
    tapa_rect = imagen_4.get_rect(center=(50,757))
    screen.blit(imagen_4, tapa_rect.topleft)
    
    draw_text(screen, f'Ángulo: {angle}', pygame.Rect(100, 780, 200, 32), font, black)
    
    #cañon_rotado
    cañon_rote = pygame.transform.rotate(imagen_2,angle)
    cañon_rect = cañon_rote.get_rect(center=(50, 738))
    screen.blit(cañon_rote, cañon_rect.topleft)
        
    # En el bucle principal, revisa los límites para dejar de mostrar la pelota
    if len(x) > 0 and len(y) > 0:
        xCoordinate = int(x.pop(0))
        yCoordinate = int(y.pop(0))
        if 0 <= yCoordinate < height:  # Asegúrate de que la pelota esté dentro de los límites visibles
            ball_rect = imagen_3.get_rect(center=(xCoordinate, height - yCoordinate))
            screen.blit(imagen_3, ball_rect.topleft)
            historial_puntos.append((xCoordinate, height - yCoordinate))
        else:
            historial_puntos.append((xCoordinate, height - yCoordinate))  # Añadir a la historia, pero no dibujar

        # Dibuja el rastro
        for i in range(len(historial_puntos) - 1):
            pygame.draw.line(screen, white, historial_puntos[i], historial_puntos[i + 1], 2)

    
    pygame.display.flip()

pygame.quit()