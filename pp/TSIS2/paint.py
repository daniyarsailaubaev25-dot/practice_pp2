import pygame
import math
import datetime

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fps = pygame.time.Clock()
pygame.display.set_caption("Paint Game (TSIS)")

drawing = False
start_pos = (0,0)
brush_size = 5

now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{time}.png"

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = [black, red, green, blue]
brush_sizes = [2, 5, 10]

current_color = black
tool = "brush"

def draw_ui():
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + 40*i, 30, 30, 30))

    for i, brush_i_size in enumerate(brush_sizes):
        pygame.draw.rect(screen, white, (720 + 60*i, 30, 34, 34))

    pygame.draw.rect(screen, black, (10, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (120, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (230, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (340, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (450, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (560, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (670, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (780, 70, 100, 50), 2)
    pygame.draw.rect(screen, black, (10, 150, 100, 50), 2)
    pygame.draw.rect(screen, black, (780, 150, 100, 50), 2)
    pygame.draw.rect(screen, black, (720, 30, 34, 34), 2)
    pygame.draw.rect(screen, black, (780, 30, 34, 34), 2)
    pygame.draw.rect(screen, black, (840, 30, 34, 34), 2)
    pygame.draw.rect(screen, black, (450, 10, 50, 50), 2)
    


    font = pygame.font.SysFont(None, 21)
    screen.blit(font.render("Brush", True, black), (30, 85))
    screen.blit(font.render("Rect", True, black), (150, 85))
    screen.blit(font.render("Circle", True, black), (250, 85))
    screen.blit(font.render("Square", True, black), (360, 85))
    screen.blit(font.render("Right Triangle", True, black), (450, 85))
    screen.blit(font.render("Eq. Triangle", True, black), (570, 85))
    screen.blit(font.render("Rhombus", True, black), (690, 85))
    screen.blit(font.render("Eraser", True, black), (810, 85))
    screen.blit(font.render("Pencil", True, black), (30, 170))
    screen.blit(font.render("Str. Line", True, black), (800, 170))
    screen.blit(font.render("2px", True, black), (723, 40))
    screen.blit(font.render("5px", True, black), (783, 40))
    screen.blit(font.render("10px", True, black), (841, 40))
    screen.blit(font.render("Fill", True, black), (465, 30))

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return
    
    stack = [(x,y)]

    while stack:
        new_x, new_y = stack.pop()

        if new_x < 0 or new_x >= WIDTH or new_y < 210 or new_y >= HEIGHT:
            continue

        if surface.get_at((new_x,new_y)) == target_color:
            surface.set_at((new_x, new_y), new_color)

            stack.append((new_x + 1, new_y))
            stack.append((new_x - 1, new_y))
            stack.append((new_x, new_y + 1))
            stack.append((new_x, new_y - 1))


canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(white)
canvas.set_clip(pygame.Rect(0, 210, WIDTH, HEIGHT - 210)) 

running = True

while True:

    screen.fill((255, 255, 255))
    fps.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos

            if y > 210:
                if tool == "fill":
                    flood_fill(canvas, x, y, current_color)
                else:
                    drawing = True
                    start_pos = event.pos
            else:
              
              drawing = False

              if pygame.Rect(10, 70, 100, 50).collidepoint(x, y): tool = "brush"
              if pygame.Rect(120, 70, 100, 50).collidepoint(x, y): tool = "rect"
              if pygame.Rect(230, 70, 100, 50).collidepoint(x, y): tool = "circle"
              if pygame.Rect(340, 70, 100, 50).collidepoint(x, y): tool = "square"
              if pygame.Rect(450, 70, 100, 50).collidepoint(x, y): tool = "right triangle"
              if pygame.Rect(560, 70, 100, 50).collidepoint(x, y): tool = "eq. triangle"
              if pygame.Rect(670, 70, 100, 50).collidepoint(x, y): tool = "rhombus"
              if pygame.Rect(780, 70, 100, 50).collidepoint(x, y): tool = "eraser"
              if pygame.Rect(10, 150, 100, 50).collidepoint(x, y): tool = "pencil"
              if pygame.Rect(780, 150, 100, 50).collidepoint(x, y): tool = "str. line"
              if pygame.Rect(450, 10, 50, 50).collidepoint(x, y): tool = "fill"

            
              for i, color in enumerate(colors):
                if pygame.Rect(10 + 40*i, 30, 30, 30).collidepoint(x, y): current_color = color
            
              for i, brush_i_size in enumerate(brush_sizes):
                if pygame.Rect(720 + 60*i, 30, 34, 34).collidepoint(x, y): brush_size = brush_i_size
            

        if event.type == pygame.MOUSEBUTTONUP:
         if drawing:
            end_pos = event.pos

            if tool == "rect":
             rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
             pygame.draw.rect(canvas, current_color, rect, brush_size)

            if tool == "circle":
                radius = int(math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))
                pygame.draw.circle(canvas, current_color, start_pos, radius, brush_size)

            if tool == "square":
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]

                side = max(abs(dx), abs(dy))

                rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                pygame.draw.rect(canvas, current_color, rect, brush_size)

            if tool == "right triangle":
                points = [start_pos, end_pos, (start_pos[0], end_pos[1])]
                pygame.draw.polygon(canvas, current_color, points, brush_size)

            if tool == "eq. triangle":
                side = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
                h = (side * math.sqrt(3)) / 2
                points = [start_pos, (start_pos[0] - side/2, start_pos[1] + h), (start_pos[0] + side/2, start_pos[1] + h)]
                pygame.draw.polygon(canvas, current_color, points, brush_size)

            if tool == "rhombus":
             x1, y1 = start_pos
             x2, y2 = end_pos
    
   
             points = [( (x1+x2)/2, y1 ), ( x2, (y1+y2)/2 ), ( (x1+x2)/2, y2 ), ( x1, (y1+y2)/2 )]
    
             pygame.draw.polygon(canvas, current_color, points, brush_size)

            if tool == "str. line":
                pygame.draw.line(canvas, current_color, start_pos, event.pos, brush_size)

         drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
                if tool == "brush":
                    pygame.draw.circle(canvas, current_color, event.pos, brush_size)

                if tool == "eraser":
                    pygame.draw.circle(canvas, white, event.pos, brush_size)

                if tool == "pencil":
                    pygame.draw.line(canvas, current_color, start_pos, event.pos, brush_size)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                pygame.image.save(canvas, filename)


    screen.blit(canvas, (0,0))
    draw_ui()

    pygame.display.update()