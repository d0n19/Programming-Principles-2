import pygame
from collections import deque

def flood_fill(surface, x, y, new_color):

    width, height = surface.get_size()
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return
    
    queue = deque([(x, y)])
    while queue:
        curr_x, curr_y = queue.popleft()
        if surface.get_at((curr_x, curr_y)) != target_color:
            continue
        surface.set_at((curr_x, curr_y), new_color)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if surface.get_at((nx, ny)) == target_color:
                    queue.append((nx, ny))

def draw_shape(surface, start, end, shape_type, color, thickness):
    x1, y1 = start
    x2, y2 = end
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    top_left = (min(x1, x2), min(y1, y2))

    if shape_type == 'line':
        pygame.draw.line(surface, color, start, end, thickness)
    elif shape_type == 'rect':
        pygame.draw.rect(surface, color, (*top_left, width, height), thickness)
    elif shape_type == 'circle':
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        radius = int(((x1 - x2)**2 + (y1 - y2)**2)**0.5) // 2
        pygame.draw.circle(surface, color, center, radius, thickness)
    elif shape_type == 'square':
        side = max(width, height)
        pygame.draw.rect(surface, color, (top_left[0], top_left[1], side, side), thickness)
    elif shape_type == 'right_triangle':
    
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], thickness)
    elif shape_type == 'equilateral_triangle':
       
        pygame.draw.polygon(surface, color, [((x1 + x2) // 2, y1), (x1, y2), (x2, y2)], thickness)
    elif shape_type == 'rhombus':
        
        points = [
            ((x1 + x2) // 2, y1), 
            (x2, (y1 + y2) // 2),
            ((x1 + x2) // 2, y2), 
            (x1, (y1 + y2) // 2)  
        ]
        pygame.draw.polygon(surface, color, points, thickness)