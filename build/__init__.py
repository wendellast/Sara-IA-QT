from rich import print
import os


def abrir_arquivos(): # Conserta depois
    try:
        os.startfile(r'C:\Users\Wendel\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar')
         
    except:
        print('Erro não consegue abrir')
    
def sistema_solar():
    from turtle import Turtle, Screen
    from math import sqrt, sin, cos, pi
    import tkinter as TK


    raio = 60

    class Astro(Turtle):
        def __init__(self, nome, tamanho, cor):
            Turtle.__init__(self)
            self.nome = nome
            self.tamanho = tamanho
            self.cor = cor

    class Estrela(Astro):
        def __init__(self, nome, tamanho, cor):
            Astro.__init__(self, nome, tamanho, cor)
            self.shape('circle')
            self.color(cor)
            self.shapesize(tamanho, tamanho)

    class Planeta(Astro):
        def __init__(self, nome, tamanho, cor, posicao_orbita):
            Astro.__init__(self, nome, tamanho, cor)
            self.posicao_orbita = posicao_orbita
            self.shape('circle')
            self.color(cor)
            self.shapesize(tamanho, tamanho,0)
            self.pencolor('black')
            self.pensize(1.5)
            self.speed('fastest')
            self.hideturtle()

        def translacao(self, angulo):
            global raio

            # Se for o planeta Plutão, sua órbita tem que ser uma elipse inclinada em relação ao Sol.
            if self.posicao_orbita == 9:
                angulo *= (10 - self.posicao_orbita)
                a = self.posicao_orbita * raio
                b = a/2
                r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)
                x = r*cos(pi*angulo/180)
                y = r*sin(pi*angulo/180)
                x1 = x*cos(30*180/pi) - y*sin(30*180/pi)
                y1 = x*sin(30*180/pi) + y*cos(30*180/pi)
                if angulo == 0:
                    self.up()
                    self.setpos(x1, y1)
                    self.down()
                    self.showturtle()
                self.setpos(x1, y1)

                # Os outros planetas não têm uma órbita inclinada em relação ao Sol.

            else:
                angulo *= (10 - self.posicao_orbita)
                a = self.posicao_orbita * raio
                b = a/2
                r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)
                x = r*cos(pi*angulo/180)
                y = r*sin(pi*angulo/180)
                if angulo == 0:
                    self.up()
                    self.setpos(x,y)
                    self.down()
                    self.showturtle()
                self.setpos(x,y)

    def main():
        tela = Screen()
        tela.bgcolor('white')
        tela.title('Sistema Solar')
        tela.tracer(2)

        sol = Estrela('Sol',2,'gold')

        mercurio = Planeta('Mercúrio', 0.3, 'gray', 1)
        venus = Planeta('Vênus', 0.5, 'darkorange', 2)
        terra = Planeta('Terra', 0.6, 'blue', 3)
        marte = Planeta('Marte', 0.4, 'red', 4)
        jupiter = Planeta('Júpiter', 1, 'sandybrown', 5)
        saturno = Planeta('Saturno', 0.9, 'goldenrod', 6)
        urano = Planeta('Urano', 0.8, 'mediumseagreen', 7)
        netuno = Planeta('Netuno', 0.7, 'steelblue', 8) 
        plutao = Planeta('Plutão', 0.2, 'peachpuff', 9)

        i = 0

        while True:
            mercurio.translacao(i) 
            venus.translacao(i)
            terra.translacao(i)
            marte.translacao(i)
            jupiter.translacao(i)
            saturno.translacao(i)
            urano.translacao(i)
            netuno.translacao(i)
            plutao.translacao(i)

            if i == 360:
                i = 0
            i += 1

   
    main()

sistema_solar2():
    import pygame
    import math
    pygame.init()

    WIDTH, HEIGHT =  800, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Planet Simulation")

    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (100, 149, 237)
    RED = (188, 39, 50)
    DARK_GREY = (80, 78, 81)

    FONT = pygame.font.SysFont("comicsans", 16)

    class Planet:
        AU = 149.6e6 * 1000
        G = 6.67428e-11
        SCALE = 250 / AU  # 1AU = 100 pixels
        TIMESTEP = 3600*24 # 1 day

        def __init__(self, x, y, radius, color, mass):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.mass = mass

            self.orbit = []
            self.sun = False
            self.distance_to_sun = 0

            self.x_vel = 0
            self.y_vel = 0

        def draw(self, win):
            x = self.x * self.SCALE + WIDTH / 2
            y = self.y * self.SCALE + HEIGHT / 2

            if len(self.orbit) > 2:
                updated_points = []
                for point in self.orbit:
                    x, y = point
                    x = x * self.SCALE + WIDTH / 2
                    y = y * self.SCALE + HEIGHT / 2
                    updated_points.append((x, y))

                pygame.draw.lines(win, self.color, False, updated_points, 2)

            pygame.draw.circle(win, self.color, (x, y), self.radius)
            
            if not self.sun:
                distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
                win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

        def attraction(self, other):
            other_x, other_y = other.x, other.y
            distance_x = other_x - self.x
            distance_y = other_y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            if other.sun:
                self.distance_to_sun = distance

            force = self.G * self.mass * other.mass / distance**2
            theta = math.atan2(distance_y, distance_x)
            force_x = math.cos(theta) * force
            force_y = math.sin(theta) * force
            return force_x, force_y

        def update_position(self, planets):
            total_fx = total_fy = 0
            for planet in planets:
                if self == planet:
                    continue

                fx, fy = self.attraction(planet)
                total_fx += fx
                total_fy += fy

            self.x_vel += total_fx / self.mass * self.TIMESTEP
            self.y_vel += total_fy / self.mass * self.TIMESTEP

            self.x += self.x_vel * self.TIMESTEP
            self.y += self.y_vel * self.TIMESTEP
            self.orbit.append((self.x, self.y))


    def main():
        run = True
        clock = pygame.time.Clock()

        sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
        sun.sun = True

        earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
        earth.y_vel = 29.783 * 1000 

        mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
        mars.y_vel = 24.077 * 1000

        mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
        mercury.y_vel = -47.4 * 1000

        venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
        venus.y_vel = -35.02 * 1000

        planets = [sun, earth, mars, mercury, venus]

        while run:
            pygame.display.update()
            clock.tick(60)
            WIN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for planet in planets:
                planet.update_position(planets)
                planet.draw(WIN)

    

        pygame.quit()
        
    main()

    
sistema_solar2()