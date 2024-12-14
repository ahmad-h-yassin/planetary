import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Planetary Gear Simulation")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 100, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Gear parameters
RADIUS_SUN = 40
RADIUS_PLANET = 40
NUM_PLANETS = 3
NUM_TEETH_SUN = 16
NUM_TEETH_PLANET = 16
NUM_TEETH_RING = NUM_TEETH_SUN + (2 * NUM_TEETH_PLANET)

# Calculate ring gear radius
RADIUS_RING = RADIUS_SUN * (NUM_TEETH_RING / NUM_TEETH_SUN)

# Control parameters
sun_speed = 0  # Initial speed
max_speed = 5
min_speed = -5

# Font for displaying speed
font = pygame.font.Font(None, 36)

def draw_gear_tooth(surface, center, start_angle, radius, tooth_height, tooth_width, color):
    """Draw a single gear tooth."""
    x1 = center[0] + radius * math.cos(start_angle)
    y1 = center[1] + radius * math.sin(start_angle)
    x2 = center[0] + (radius + tooth_height) * math.cos(start_angle)
    y2 = center[1] + (radius + tooth_height) * math.sin(start_angle)
    
    # Tooth tip points
    x3 = x2 + tooth_width * math.cos(start_angle + math.pi/2)
    y3 = y2 + tooth_width * math.sin(start_angle + math.pi/2)
    x4 = x2 - tooth_width * math.cos(start_angle + math.pi/2)
    y4 = y2 - tooth_width * math.sin(start_angle + math.pi/2)
    
    pygame.draw.polygon(surface, color, 
        [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

def draw_gear(surface, center, radius, num_teeth, tooth_height, tooth_width, color, rotation_angle=0):
    """Draw a complete gear with teeth."""
    # Draw the gear base circle
    pygame.draw.circle(surface, color, center, radius, 2)
    
    # Draw each tooth
    for i in range(num_teeth):
        tooth_angle = (2 * math.pi * i / num_teeth) + rotation_angle
        draw_gear_tooth(surface, center, tooth_angle, radius, tooth_height, tooth_width, color)

def calculate_planet_position(center, ring_radius, planet_radius, planet_num, total_planets, sun_angle):
    """Calculate the position of a planet gear."""
    # Position planets around the ring
    planet_angle = sun_angle + (2 * math.pi * planet_num / total_planets)
    
    # Position planets to mesh with sun gear
    x = center[0] + (ring_radius - planet_radius) * math.cos(planet_angle)
    y = center[1] + (ring_radius - planet_radius) * math.sin(planet_angle)
    
    return (int(x), int(y))

def calculate_rotations(sun_angle):
    """
    Calculate realistic rotations for planetary gears.
    
    Planetary gear kinematic equation:
    Ωring = 0
    Ωsun * Zsun = -Ωplanet * Zplanet
    Ωplanet = -Ωsun * (Zsun / Zplanet)
    """
    # Sun gear rotation
    sun_rotation = -math.degrees(sun_angle)
    
    # Planet gear rotation 
    # The planets rotate in the opposite direction of the sun gear
    # and at a different rate based on the gear tooth ratios
    planet_rotation = sun_rotation * (NUM_TEETH_SUN / NUM_TEETH_PLANET)
    
    return sun_rotation, planet_rotation

def draw_speed_control():
    """Draw speed control knob and current speed indicator."""
    # Knob background
    pygame.draw.rect(screen, GRAY, (50, 700, 700, 50))
    
    # Speed indicator
    speed_text = font.render(f"Sun Gear Speed: {sun_speed:.2f}", True, BLACK)
    screen.blit(speed_text, (300, 660))
    
    # Knob marker
    knob_x = 50 + ((sun_speed - min_speed) / (max_speed - min_speed)) * 700
    pygame.draw.circle(screen, RED, (int(knob_x), 725), 25)

# Main loop
def main():
    global sun_speed
    sun_angle = 0
    dragging_speed = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Handle mouse events for speed control
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] <= 750 and 700 <= event.pos[1] <= 750:
                    dragging_speed = True
                    # Calculate speed based on mouse x position
                    sun_speed = min_speed + (event.pos[0] - 50) / 700 * (max_speed - min_speed)
            
            if event.type == pygame.MOUSEBUTTONUP:
                dragging_speed = False
            
            if event.type == pygame.MOUSEMOTION and dragging_speed:
                # Update speed while dragging
                if 50 <= event.pos[0] <= 750:
                    sun_speed = min_speed + (event.pos[0] - 50) / 700 * (max_speed - min_speed)
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Calculate rotations
        sun_rotation, planet_rotation = calculate_rotations(sun_angle)
        
        # Draw ring gear (fixed)
        draw_gear(screen, CENTER, RADIUS_RING, NUM_TEETH_RING, 10, 15, BLUE)
        
        # Draw sun gear (rotating)
        draw_gear(screen, CENTER, RADIUS_SUN, NUM_TEETH_SUN, 10, 15, RED, math.radians(-1*sun_rotation))
        
        # Draw planet gears
        for i in range(NUM_PLANETS):
            # Calculate planet position 
            planet_pos = calculate_planet_position(CENTER, RADIUS_RING, RADIUS_PLANET, i, NUM_PLANETS, sun_angle)
            
            # Draw planet gear with its calculated rotation
            draw_gear(screen, planet_pos, RADIUS_PLANET, NUM_TEETH_PLANET, 10, 15, GREEN, math.radians(planet_rotation))
        
        # Draw speed control
        draw_speed_control()
        
        # Update the display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(60)
        
        # Update sun gear angle based on speed
        sun_angle += math.radians(sun_speed)

if __name__ == "__main__":
    main()
