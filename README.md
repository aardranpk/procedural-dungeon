# Procedural Dungeon Crawler

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.3-brightgreen)
![Version](https://img.shields.io/badge/Version-v1.2.1-yellow)

## Overview

This is a **Python-based procedural dungeon crawler** demonstrating:

- Procedural dungeon generation
- Smooth player movement
- Camera system with smooth following
- Modular code structure for scalability
- Player collision with walls and map boundaries
- Simple enemy AI
- Health bar / HUD system

This project is designed as a **professional portfolio piece** showcasing **Python programming, game development fundamentals, and clean code organization**.

---

## Project Structure



src/
<br>├── main.py # Main game loop
<br>├── dungeon/
<br>│ ├── init.py
<br>│ └── generator.py # Procedural dungeon generation
<br>├── entities/
<br>│ ├── init.py
<br>│ └── player.py # Player class and movement
<br>└── systems/
<br>├── init.py
<br>└── camera.py # Camera system for smooth scrolling


---

## Controls

- **Arrow Keys** – Move the player  
- **ESC / Close Window** – Exit game

---

## Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>/src

```
2. **Install Dependencies:**
```bash
pip install pygame
```
3. **Run the game:**
```bash
python main.py
```
## Version History

v1.0.0 – Initial release: procedural dungeon generation and player movement

v1.1.0 – Added camera system for smooth map scrolling, updated README

v1.2.0 – Smooth camera movement (lerp), player collision with walls, added simple enemy

v1.2.1 – Added health bar/HUD, enforced map boundaries, improved tile graphics

## Features

Camera System: Smooth following with linear interpolation (lerp)

Collision: Player and enemy cannot move through walls

Enemy AI: Simple random movement

Health Bar / HUD: Displays player health above the sprite

Tile Visuals: Distinct coloring for floors, walls, and special tiles

Clean, Modular Code: Easy to extend with new features

## Future Plans

Add more complex enemy AI and combat system

Introduce items, collectibles, and power-ups

Implement interactive NPCs or quests

Optimize performance for larger maps

Add animations and polished graphics

## Author

Aardran Premakumar