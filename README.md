# Procedural Dungeon Crawler

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.3-brightgreen)
![Version](https://img.shields.io/badge/Version-v1.1.0-yellow)

## Overview

This is a **Python-based procedural dungeon crawler** demonstrating:

- Procedural dungeon generation
- Smooth player movement
- Modular code structure for scalability
- Camera system to follow the player in large maps

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

v1.1.0 – Added camera system for smooth scrolling and improved visuals

## Future Plans

Add enemies, NPCs, and items

Implement more advanced dungeon generation algorithms

Add combat and interactive systems

Optimize camera with smooth lerp transitions

## Author

Aardran Premakumar