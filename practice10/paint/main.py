import pygame
import sys 
pygame.init()

width, height = 900,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = [black, red, green, blue]

current_color = black
tool = "brush"

drawing = False
start_pos = (0,0)

screen.fill(white)

def draw_ui():
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))
    
    pygame.draw.rect(screen, black, (10,60,80,30),2)
    pygame.draw.rect(screen, black, (100, 60, 80, 30), 2)
    pygame.draw.rect(screen, black, (190,60,80,30),2)
    pygame.draw.rect(screen, black, (280,60,80,30), 2)
    
    font = pygame.font.Font(None, 24)
    screen.blit(font.render("Brush", True, black), (15,65))
    screen.blit(font.render("Rect", True, black), (110, 65))
    screen.blit(font.render("Circle", True, black), (200, 65))
    screen.blit(font.render("Eraser", True, black), (285,65))
    
canvas = pygame.Surface((width, height))
canvas.fill(white)

running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            
            for i, color in enumerate(colors):
                if pygame.Rect(10 + i*40, 10, 30, 30).collidepoint(x,y):
                    current_color = color
            if pygame.Rect(10,60,80,30).collidepoint(x,y):
                tool = "brush"
            if pygame.Rect(100,60,80,30).collidepoint(x,y):
                tool = "rect"
            if pygame.Rect(190,60,80,30).collidepoint(x,y):
                tool = "circle"
            if pygame.Rect(280,60,80,30).collidepoint(x,y):
                tool = "eraser"
                
            drawing = True
            start_pos = event.pos 
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            
            if tool == "rect":
                rect = pygame.Rect(start_pos,(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(canvas, current_color, rect, 2)
                
            if tool == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(canvas,current_color, start_pos, radius, 2)
                
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(canvas, current_color, event.pos, 5)
            if tool == "eraser":
                pygame.draw.circle(canvas, white, event.pos, 10)
                
    screen.fill(white)
    screen.blit(canvas, (0,0))
    draw_ui()
    
    pygame.display.update()
    
pygame.quit()
sys.exit()
                
                