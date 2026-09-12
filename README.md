# Pacman Game Project (HKUST COMP1021)

A complete retro-arcade **Pacman** implementation developed in Python using the standard `turtle` graphics library. This project was developed as the culminating programming assignment for the **COMP1021: Introduction to Computer Science** course at the Hong Kong University of Science and Technology (HKUST).

The game faithfully recreates the classic arcade experience, featuring smooth custom-rendered vector animations, tile-based pathfinding logic, collision detection algorithms, screen wrapping (tunnels), multi-agent ghost behaviors, real-time score tracking, and custom game state mechanics.

---

## 🎮 Key Features & Highlights

### 1. Dynamic Procedural Animation & Rendering
- **Pacman Chomping Animation:** Procedurally renders Pacman using trigonometric arc calculations with a variable opening angle (expanding and contracting between $0^\circ$ and $40^\circ$), seamlessly oriented in 4 cardinal directions.
- **Directional Animated Ghosts:** 4 distinct ghosts (`Blinky`, `Pinky`, `Inky`, `Clyde`) dynamically drawn with custom polygonal bodies and pupils that actively track their current heading.
- **Matrix-Driven Map Rendering:** Procedurally parses a 2D tile map string array to construct a custom maze ($21 \times 19$ grid) complete with perimeter borders, pathways, pellets, and power pellets.

### 2. Core Game Loop & Motion Logic
- **Fixed Frame-Rate Game Loop:** Driven by asynchronous timer interrupts (`turtle.ontimer`) running at ~30 FPS with screen updates buffered via `turtle.tracer(False)`.
- **Grid-Aligned Movement Buffer:** Prevents desynchronization by buffering user direction inputs and only executing turns when Pacman aligns cleanly with grid intersections (`tile_size = 30`).
- **Screen-Wrapping Tunnels:** Seamless horizontal and vertical world-wrapping algorithms that teleport entities across opposite boundaries.

### 3. AI & Entity Mechanics
- **Ghost Decision-Making Logic:** Ghosts evaluate valid non-wall adjacent tiles at intersections and pick randomized directions while intelligently suppressing $180^\circ$ reverse-turns (preventing rapid back-and-forth oscillation unless stuck in a dead-end).
- **Collision Detection Pipeline:** Implements Axis-Aligned Bounding Box (AABB) / Manhattan distance-based proximity math to detect wall collisions, food consumption, and fatal ghost contact.
- **God-Mode / Cheat Toggle:** Toggleable invincibility mode (triggered by the `C` key), dynamically swapping Pacman's color to green and bypassing fatality checks.

---

## 🛠️ Technical Skills Demonstrated

This project showcases fundamental and intermediate software engineering principles in Python:

| Category | Skills & Concepts Applied |
| :--- | :--- |
| **Language Fundamentals** | Data structures (`list`, `dict`, 2D matrix representations), string slicing / mutation, scope management (`global` state handlers), modular decomposition. |
| **Game Architecture** | Non-blocking event-driven loop architecture, frame throttling, dynamic redraw pipelines, finite game-state transitions (`Playing`, `Game Over`, `You Win`). |
| **Algorithms & Math** | 2D coordinate space transformations, Euclidean/Manhattan distance calculations, directional vector resolution, random multi-choice decision engines. |
| **Event Handling & GUI** | Asynchronous keyboard event binding (`onkeypress`, `listen`), double-buffered procedural vector rendering via Python's standard `turtle` graphics engine. |
| **Defensive Programming** | Grid snapping and boundary clamping to prevent out-of-bounds wall clipping or graphical desync. |

---

## 🕹️ Controls & Mechanics

| Key | Action |
| :---: | :--- |
| `↑` `↓` `←` `→` | Control Pacman's movement direction |
| `C` | Toggle **Invincibility Cheat Mode** (Pacman turns green and immune to ghosts) |

### Scoring
- **Pellet (`.`):** `+1` Point
- **Power Pellet (`o`):** `+5` Points
- **Win Condition:** Clear all pellets from the maze.
- **Loss Condition:** Colliding with any ghost while not in Cheat Mode.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6+ (Standard installation includes `turtle`, `math`, and `random`). No external pip dependencies required.

### Installation & Execution
1. Clone this repository:
   ```bash
   git clone https://github.com/SIN-Chun-Hung/pacman-game-python.git
   cd pacman-game-python
   ```
2. Run the game:
   ```bash
   python "pacman-game-python.py"
   ```

---

## 📂 Project Structure

```text
├── pacman-game-python.py    # Main executable Python source code containing complete game logic
└── README.md                # Project documentation and portfolio profile
```