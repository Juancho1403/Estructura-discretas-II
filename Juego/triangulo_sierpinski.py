# Librerías a utilizar en el proyecto
import turtle

# Función para dibujar un triángulo utilizando turtle graphics
def dibujarTriangulo(puntos, color, miTortuga):
    # Establece el color de relleno
    miTortuga.fillcolor(color)
    
    # Levanta el lápiz y mueve a la primera posición sin dibujar
    miTortuga.up()
    miTortuga.goto(puntos[0][0], puntos[0][1])
    miTortuga.down()
    
    # Comienza a rellenar el triángulo
    miTortuga.begin_fill()
    
    # Dibuja el triángulo conectando los tres puntos
    miTortuga.goto(puntos[1][0], puntos[1][1])
    miTortuga.goto(puntos[2][0], puntos[2][1])
    miTortuga.goto(puntos[0][0], puntos[0][1])
    
    # Termina el relleno del triángulo
    miTortuga.end_fill()

# Función para obtener el punto medio entre dos puntos dados
def obtenerMitad(p1, p2):
    # Calcula las coordenadas del punto medio entre p1 y p2
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Función recursiva para generar el fractal de Sierpinski
def sierpinski(puntos, grado, miTortuga):
    # Paleta de colores personalizada para diferentes niveles de recursión
    paleta_colores = ['#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#3CB371']
    
    # Selecciona un color de la paleta según el nivel actual (grado)
    color = paleta_colores[grado % len(paleta_colores)]
    
    # Dibuja el triángulo de este nivel con el color correspondiente
    dibujarTriangulo(puntos, color, miTortuga)
    
    # Condición base: si grado es mayor a cero, continuar subdividiendo
    if grado > 0:
        # Subdivide el triángulo en tres triángulos más pequeños
        # y reduce el grado de recursión en 1
        sierpinski(
            [puntos[0],
             obtenerMitad(puntos[0], puntos[1]),
             obtenerMitad(puntos[0], puntos[2])],
            grado - 1, miTortuga
        )
        sierpinski(
            [puntos[1],
             obtenerMitad(puntos[0], puntos[1]),
             obtenerMitad(puntos[1], puntos[2])],
            grado - 1, miTortuga
        )
        sierpinski(
            [puntos[2],
             obtenerMitad(puntos[2], puntos[1]),
             obtenerMitad(puntos[0], puntos[2])],
            grado - 1, miTortuga
        )

# Función principal que configura la pantalla y ejecuta el dibujo del fractal
def main():
    # Inicializa el objeto Turtle
    miTortuga = turtle.Turtle()
    
    # Configura la ventana de Turtle y establece el título
    miVentana = turtle.Screen()
    miVentana.title("Triángulo de Sierpinski")
    
    # Ajusta la velocidad de dibujo para hacerlo rápido
    miTortuga.speed(0)
    
    # Define los puntos iniciales para el triángulo grande
    misPuntos = [[-200, -100], [0, 200], [200, -100]]
    
    # Llama a la función sierpinski para empezar el fractal
    sierpinski(misPuntos, 4, miTortuga)
    
    # Espera hasta que el usuario haga clic para cerrar la ventana
    miVentana.exitonclick()

# Ejecuta el programa
main()
