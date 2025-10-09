import pygame
import pymunk
import numpy as np

# Physics Constants
GRAVITY = 9.81
FPS = 60

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Window settings
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Initialize Physics
space = pymunk.Space()
space.gravity = (0, -GRAVITY)

# Sound parameters
def create_sound(frequency):
    sample_rate = 44100
    duration = 1  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return pygame.sndarray.make_sound((wave * 32767).astype(np.int16))

# Sound associated with a vibration
vibration_sound = create_sound(440)  # A4 note (440 Hz)

class SandParticle:
    def __init__(self, position):
        mass = 1
        radius = 5
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1.0
        space.add(self.body, self.shape)

    def update(self):
        # Check for vibration (simple example)
        if self.body.velocity.get_distance((0, 0)) > 100:  # Change threshold as needed
            vibration_sound.play()

# Create sand particles
particles = [SandParticle((400 + i * 20, 500)) for i in range(20)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update physics
    space.step(1 / FPS)

    # Clear screen
    screen.fill((255, 255, 255))

    # Update particles
    for particle in particles:
        particle.update()
        pygame.draw.circle(screen, (0, 0, 0), (int(particle.body.position.x), 600 - int(particle.body.position.y)), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
