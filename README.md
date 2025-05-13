# Asteroids

A simple arcade-style game based on the classic Asteroids, built with Pygame.

## Overview

This project is a modern implementation of the classic Asteroids arcade game. Players control a triangular spaceship, navigating through an asteroid field while shooting and destroying asteroids.

## Features

- Smooth ship movement with rotation and thrust controls
- Asteroid field that continuously spawns new challenges
- Collision detection between shots, asteroids, and player
- Asteroids split into smaller pieces when hit

## Requirements

- Python 3.x
- Pygame 2.6.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/stkisengese/asteroids.git
cd asteroids
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

Run the game:
```bash
python main.py
```

### Controls
- W: Move forward
- S: Move backward
- A: Rotate left
- D: Rotate right
- SPACE: Shoot

## Project Structure

- `main.py`: Game initialization and main loop
- `player.py`: Player ship implementation
- `asteroid.py`: Asteroid object implementation
- `asteroidfield.py`: Controls asteroid spawning
- `shot.py`: Player projectile implementation
- `circleshape.py`: Base class for circular game objects
- `constants.py`: Game constants and configuration

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Stephen Kisengese - [stkisengese](https://github.com/stkisengese)
