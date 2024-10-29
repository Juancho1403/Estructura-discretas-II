# Librerías a utilizar en el proyecto
import pygame
import math

# Inicializa pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego Triángulo de Pascal")

# Colores
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255)]
bg_color = (30, 30, 30)
screen.fill(bg_color)

# Función para calcular el coeficiente binomial
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return math.comb(n, k)

# Dibujar el triángulo de Pascal
def dibujarTrianguloPascal(nivel, mod):
    screen.fill(bg_color)
    base_y = 20  # Posición y inicial
    base_x = width // 2  # Centrado horizontal

    for n in range(nivel):
        x = base_x - (n * 20 // 2)  # Centrado para cada nivel
        y = base_y + n * 20  # Altura de cada nivel

        for k in range(n + 1):
            coef = binomial(n, k) % mod  # Calcular el valor y aplicar el módulo
            color = colors[coef % len(colors)]  # Selección de color según el módulo
            
            # Dibuja el círculo de cada coeficiente
            pygame.draw.circle(screen, color, (x, y), 10)
            x += 20  # Espacio entre los valores en el nivel

# Configuración inicial
nivel = 20  # Número de filas en el triángulo de Pascal
mod = 5  # Módulo para patrones de color
running = True

# Ciclo del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Cambiar el módulo y reiniciar el dibujo
            if event.key == pygame.K_UP:
                mod = (mod % len(colors)) + 1
                dibujarTrianguloPascal(nivel, mod)
            elif event.key == pygame.K_DOWN:
                mod = max(1, mod - 1)
                dibujarTrianguloPascal(nivel, mod)
            elif event.key == pygame.K_RIGHT:
                nivel = min(40, nivel + 1)  # Limitar el número de filas para no sobrecargar
                dibujarTrianguloPascal(nivel, mod)
            elif event.key == pygame.K_LEFT:
                nivel = max(5, nivel - 1)  # Limitar para que no sea negativo
                dibujarTrianguloPascal(nivel, mod)

    pygame.display.flip()

# Cerrar pygame
pygame.quit()
