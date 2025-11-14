# Turtle Crossing 🐢

A classic arcade-style game re-created with Python’s `turtle` graphics module. Guide the turtle across the road, dodge the oncoming cars, and level up as traffic gets faster.

## Features
- Frogger-inspired gameplay built entirely with the standard library
- Random car spawning and increasing speed after each successful crossing
- Scoreboard that tracks current level and displays a clear game-over message
- Modular structure to keep gameplay logic easy to follow and extend

## Controls
- `Up Arrow`: Move the turtle forward  
The turtle resets to the start whenever you reach the finish line.

## Project Structure
- `main.py`: Initializes the screen, listens for input, and runs the main loop.
- `body.py`: Defines the player turtle, movement rules, and reset behavior.
- `cars.py`: Handles car creation, movement, and speed scaling per level.
- `scoreboard.py`: Tracks the player’s level and renders HUD/game-over text.

## Getting Started
1. Ensure Python 3.x is installed (the `turtle` module ships with Python).
2. Clone or download this repository.
3. From the project root, run:

   ```bash
   python main.py
   ```

Enjoy dodging traffic and see how many levels you can conquer!

## Contributing
Ideas for new mechanics, graphics, or optimizations are welcome—fork the repo, make your improvements, and open a pull request.
