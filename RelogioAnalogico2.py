import pygame
import math
import time

# Inicialização do Pygame
pygame.init()

# Definindo o tamanho da tela
screen = pygame.display.set_mode((1050, 1050))

# Definindo as cores
black = (0, 0, 0)
white = (255, 255, 255)
deepPink = (255, 20, 147)
gold = (255, 215, 0)
royalBlue = (65, 105, 225)
seaGreen = (46, 139, 87)

# Definindo o tamanho e posição do relógio
clock_radius = 400
clock_center = (525, 525)

# Loop principal
while True:
    # Obtendo a hora atual
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Pintando o fundo da tela
    screen.fill(black)

    # Desenhando o círculo externo do relógio
    pygame.draw.circle(screen, seaGreen, clock_center, clock_radius, 10)

    # Desenhando os números no relógio
    font = pygame.font.Font(None, 120)
    for i in range(1, 13):
        angle = math.pi / 6 * i
        x = clock_center[0] + math.sin(angle) * (clock_radius - 60)
        y = clock_center[1] - math.cos(angle) * (clock_radius - 60)
        text = font.render(str(i), True, gold)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    # Desenhando o ponteiro das horas
    hour_angle = math.pi / 6 * (hour % 12) + math.pi / 360 * minute
    hour_x = clock_center[0] + math.sin(hour_angle) * (clock_radius - 200)
    hour_y = clock_center[1] - math.cos(hour_angle) * (clock_radius - 200)
    pygame.draw.line(screen, white, clock_center, (hour_x, hour_y), 12)

    # Desenhando o ponteiro dos minutos
    minute_angle = math.pi / 30 * minute
    minute_x = clock_center[0] + math.sin(minute_angle) * (clock_radius - 100)
    minute_y = clock_center[1] - math.cos(minute_angle) * (clock_radius - 100)
    pygame.draw.line(screen, royalBlue, clock_center, (minute_x, minute_y), 8)

    # Desenhando o ponteiro dos segundos
    second_angle = math.pi / 30 * second
    second_x = clock_center[0] + math.sin(second_angle) * (clock_radius - 50)
    second_y = clock_center[1] - math.cos(second_angle) * (clock_radius - 50)
    pygame.draw.line(screen, deepPink, clock_center, (second_x, second_y), 4)

    # Atualizando a tela
    pygame.display.flip()

    # Esperando um pouco antes de atualizar novamente
    pygame.time.wait(100)

    # Verificando se o usuário quer sair
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
