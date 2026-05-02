import pygame
import datetime
from tools import flood_fill, draw_shape


pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2: Paint Pro")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

canvas = pygame.Surface((WIDTH, HEIGHT - 120))
canvas.fill(WHITE)

current_color = BLACK
thickness = 2
tool = 'pencil' 
is_drawing = False
start_pos = (0, 0)

font = pygame.font.SysFont("Arial", 16)
bold_font = pygame.font.SysFont("Arial", 16, bold=True)

def save_canvas():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"paint_export_{timestamp}.png"
    pygame.image.save(canvas, filename)
    print(f"Файл сохранен как {filename}")

running = True
while running:
    
    screen.fill(GRAY)
    screen.blit(canvas, (0, 0)) 
    
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_p: tool = 'pencil'
            if event.key == pygame.K_l: tool = 'line'
            if event.key == pygame.K_r: tool = 'rect'
            if event.key == pygame.K_c: tool = 'circle'
            if event.key == pygame.K_s: tool = 'square'
            if event.key == pygame.K_t: tool = 'right_triangle'
            if event.key == pygame.K_e: tool = 'equilateral_triangle'
            if event.key == pygame.K_h: tool = 'rhombus'
            if event.key == pygame.K_f: tool = 'fill'
            
        
            if event.key == pygame.K_1: current_color = BLACK
            if event.key == pygame.K_2: current_color = RED
            if event.key == pygame.K_3: current_color = BLUE
            if event.key == pygame.K_4: current_color = GREEN
            if event.key == pygame.K_5: current_color = WHITE 
            
    
            if event.key == pygame.K_UP: thickness += 1
            if event.key == pygame.K_DOWN: thickness = max(1, thickness - 1)
            
        
            if event.key == pygame.K_TAB:
                save_canvas()

        if event.type == pygame.MOUSEBUTTONDOWN:
          
            if mouse_pos[1] < HEIGHT - 120:
                if tool == 'fill':
                    flood_fill(canvas, *mouse_pos, current_color)
                else:
                    is_drawing = True
                    start_pos = mouse_pos

        if event.type == pygame.MOUSEBUTTONUP:
            if is_drawing and tool != 'pencil':
     
                draw_shape(canvas, start_pos, mouse_pos, tool, current_color, thickness)
            is_drawing = False

        if event.type == pygame.MOUSEMOTION:
            if is_drawing and tool == 'pencil':
            
                pygame.draw.line(canvas, current_color, start_pos, mouse_pos, thickness)
                start_pos = mouse_pos

    if is_drawing and tool != 'pencil':
        draw_shape(screen, start_pos, mouse_pos, tool, current_color, thickness)

    pygame.draw.rect(screen, (200, 200, 200), (0, HEIGHT - 120, WIDTH, 120))
 
    pygame.draw.rect(screen, current_color, (20, HEIGHT - 100, 40, 40))
    pygame.draw.rect(screen, BLACK, (20, HEIGHT - 100, 40, 40), 2)
  
    info_text = f"Инструмент: {tool.upper()} | Толщина: {thickness} | TAB: Сохранить"
    color_hint = "Цвета: 1: Черный, 2: Красный, 3: Синий, 4: Зеленый, 5: Ластик"
    shape_hint = "P: Карандаш, L: Линия, R: Прямоугольник, C: Круг, S: Квадрат, T/E: Треугольники, H: Ромб, F: Заливка"
    
    screen.blit(bold_font.render(info_text, True, BLACK), (80, HEIGHT - 100))
    screen.blit(font.render(color_hint, True, BLACK), (80, HEIGHT - 75))
    screen.blit(font.render(shape_hint, True, (50, 50, 50)), (20, HEIGHT - 40))

    pygame.display.flip()

pygame.quit()