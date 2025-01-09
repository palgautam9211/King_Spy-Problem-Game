# King_Spy-Problem-Game
```markdown
# King and Spy Game

## Project Description
The project is a grid-based strategy game where players experience a dynamic chase. A king starts on a randomly assigned cell within a grid and must navigate toward the grid's edge after collecting a treasure. Two spy agents continuously pursue the king, aiming to catch him before he escapes. Each turn involves strategic moves by the king and spies, with the treasure introducing an additional objective and escape condition for the king. The game combines randomness with tactical decision-making, ensuring an engaging and unpredictable experience.

## Features
- **Dynamic Gameplay:** The king and spies move each turn, creating a dynamic chase sequence.
- **Randomized Setup:** The initial positions of the king, spies, and treasure are randomized to ensure a unique game every time.
- **Treasure Objective:** The king must collect the treasure before attempting to escape the grid.
- **Strategic Decisions:** The spies move strategically to intercept the king, adding a layer of challenge.

## How to Play
1. Run the game script.
2. Watch the king, spies, and treasure interact on the grid.
3. The game ends when:
   - The king escapes with the treasure.
   - The spies catch the king.

## Technologies Used
- **Python:** The game logic and grid-based simulation are implemented in Python.
- **Random Module:** For generating random positions and movements.
- **Time Module:** To create delays between moves, enhancing the simulation experience.

## Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/palgautam9211/King_Spy-Problem-Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd King_Spy-Problem-Game
   ```
3. Run the game:
   ```bash
   python king_spy_game.py
   ```

## Rules
- The king can move one cell in any direction (up, down, left, right) each turn.
- The spies move toward the king, attempting to intercept him.
- The king wins by collecting the treasure and escaping the grid's edge.
- The spies win by catching the king.

## Future Enhancements
- Add more spies or obstacles to increase difficulty.
- Introduce a scoring system based on the number of moves.
- Allow user input to control the spies or king.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as per the license terms.
```

