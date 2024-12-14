# Planetary Gears Simulation

## Overview

This project provides a visual simulation of planetary gears using Python and the Pygame library. Planetary gears are commonly used in mechanical systems, such as automatic transmissions and robotics, due to their compact design and efficiency. This simulation allows users to interact with a planetary gear system by controlling the speed of the sun gear and observing how the planet and ring gears move.

## Features

- Visual representation of a planetary gear system.
- Interactive controls for adjusting the speed of the sun gear.
- Real-time simulation of gear interactions.

## Components

- **Sun Gear**: The central gear around which the planet gears orbit.
- **Planet Gears**: Gears that mesh with both the sun and ring gears.
- **Ring Gear**: An outer gear that meshes with the planet gears and encloses the system.

## Requirements

To run the simulation, you need to have the following dependencies installed:

- Python 3.x
- Pygame library

### Install Dependencies

1. Install Python from the official website: [Python Downloads](https://www.python.org/downloads/).
2. Install Pygame using pip:
   ```
   pip install pygame
   ```

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:
```
git clone https://github.com/yourusername/planetary.git
cd planetary
```

### 2. Run the Simulation

Once you have installed Python and Pygame, you can run the simulation by executing the following command in the project directory:
```
python planetary_gears.py
```

This will open a Pygame window showing the planetary gear system. Use your mouse to adjust the speed of the sun gear and observe the movement of the planet and ring gears in real-time.

### 3. Code Structure

The project is organized as follows:
```
planetary-gears/
│
├── planetary_gears.py  # Main Python file for simulation
├── README.md           # Project documentation
```

### 4. Customizing the Simulation

You can modify the simulation by adjusting the parameters such as gear sizes, tooth counts, and speed settings. The code is structured to allow easy modifications to the gear system.

## Example Interaction

Upon running the simulation, you will see a window displaying the following:

- **The Sun Gear** at the center.
- **Planet Gears** revolving around the sun gear.
- **The Ring Gear** surrounding the planet gears.
  
You can adjust the speed of the sun gear by moving your mouse, which will update the speed of the planet and ring gears accordingly.

## Conclusion

This planetary gear simulation provides a hands-on way to understand how planetary gear systems work. By interacting with the simulation, you can visualize the relationships between the different gears and observe their motions in real time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
