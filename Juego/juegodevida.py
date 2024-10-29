# Librerías a utilizar en el proyecto
import pygame as py
import numpy as np
import time

# Inicio pygame
py.init()

# Ancho y Largo de la ventana del juego
width, height = 890, 500
py.display.set_caption("Juego de la Vida")
screen = py.display.set_mode((width, height))

# Color del fondo
bg = (25, 25, 25)
screen.fill(bg)

# Número de celdas
nxC, nyC = 50, 50

# Dimensiones de cada celda
cell_width = width / nxC
cell_height = height / nyC

# Estado de las celdas. Vivas = 1; Muertas = 0
game_state = np.zeros((nxC, nyC))

# Crear patrones iniciales (ej., nave, parpadeador, etc.)
patterns = {
    "movil": [(21, 21), (22, 22), (22, 23), (21, 23), (20, 23)],
    "estatico": [(5, 5), (5, 6), (6, 5), (6, 6)],
    "nave": [(10, 10), (10, 11), (10, 12), (11, 9), (11, 13)],
    "mariposa": [(15, 15), (15, 16), (15, 17), (16, 14), (16, 18), (17, 15), (17, 16), (17, 17)],
    "planeador": [(25, 25), (25, 26), (25, 27), (26, 25), (27, 26)],
    "marciano": [(30, 30), (30, 31), (30, 32), (31, 30), (31, 31), (31, 32), (32, 30), (32, 31), (32, 32)],
    "parpadeador": [(40, 40), (40, 41), (40, 42)],
    "pentadecathlon": [(35, 35), (35, 36), (35, 37), (36, 35), (36, 36), (36, 37), (37, 35), (37, 36), (37, 37), (35, 38), (36, 38), (37, 38)]
}

# Activar celdas de los patrones iniciales
for pattern in patterns.values():
    for (x, y) in pattern:
        game_state[x, y] = 1

# Control de la ejecución del juego
running = True
paused = False
generation = 0  # Contador de generaciones

# Fuente para mostrar texto en pantalla
font = py.font.SysFont("Arial", 18)

while running:
    # Capturar eventos
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                paused = not paused
            elif event.key == py.K_r:
                # Reiniciar juego
                game_state = np.zeros((nxC, nyC))
                generation = 0
        elif py.mouse.get_pressed()[0]:
            posX, posY = py.mouse.get_pos()
            cellX, cellY = int(posX // cell_width), int(posY // cell_height)
            game_state[cellX, cellY] = not game_state[cellX, cellY]

    # Mostrar información en pantalla
    screen.fill(bg)
    text_gen = font.render(f"Generación: {generation}", True, (180, 180, 180))
    text_controls = font.render("Espacio: Pausar/Continuar | R: Reiniciar", True, (180, 180, 180))
    screen.blit(text_gen, (10, 10))
    screen.blit(text_controls, (10, 30))

    # Lógica del Juego de la Vida
    if not paused:
        new_game_state = np.copy(game_state)
        generation += 1  # Incrementar generación

        for y in range(0, nxC):
            for x in range(0, nyC):
                # Contar vecinos vivos
                neighbors = sum(
                    [game_state[(x + i) % nxC, (y + j) % nyC]
                     for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == 0 and j == 0)]
                )

                # Reglas del Juego de la Vida
                # Regla 1: Una célula muerta con exactamente 3 vecinos vivos revive
                if game_state[x, y] == 0 and neighbors == 3:
                    new_game_state[x, y] = 1
                # Regla 2: Una célula viva con menos de 2 o más de 3 vecinos vivos muere
                elif game_state[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                    new_game_state[x, y] = 0

                # Establecer color de la celda (blanco para vivas, gris para muertas)
                color = (255, 255, 255) if new_game_state[x, y] == 1 else (128, 128, 128)
                poly = [
                    ((x) * cell_width, (y) * cell_height),
                    ((x + 1) * cell_width, (y) * cell_height),
                    ((x + 1) * cell_width, (y + 1) * cell_height),
                    ((x) * cell_width, (y + 1) * cell_height)
                ]
                py.draw.polygon(screen, color, poly, 0 if new_game_state[x, y] == 1 else 1)

        # Actualizar estado del juego
        game_state = np.copy(new_game_state)

    # Actualizar la pantalla
    py.display.flip()

# Salir de pygame
py.quit()
