# Recycle Game
## How to Run
1. Clone this repository:
  https://github.com/Nivedhitha-Duggi/recycle.git

A fun, interactive game where the player collects falling bottles and avoids thorns. The goal is to progress through three levels by collecting a specific number of bottles. The game increases in difficulty with each level, featuring faster falling items and new challenges.

## Features
- **Multiple Levels**: The game has three levels, each with increasing difficulty.
- **Player Movement**: The player can move left or right to collect bottles and avoid thorns.
- **Falling Items**: Bottles fall from the top of the screen, and the player needs to collect them. Thorns also fall, and touching them will result in losing a life.
- **Score System**: The player must collect a set number of bottles to advance to the next level.
- **Game Over Condition**: The game ends when the player loses all lives or completes all levels.
- **Background Music**: The game includes background music that plays throughout.

## Requirements

- **Python 3.x** (preferably Python 3.7 or above)
- **Pygame**: A library used to create the game.

## Installation

### 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Nivedhitha-Duggi/recycle_game.git
2. Set up a virtual environment (optional but recommended)
Navigate to the project folder:

bash
Copy code
cd recycle_game
Then, create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
3. Install the required dependencies
Run the following command to install Pygame:

bash
Copy code
pip install pygame
4. Download game assets
Make sure you have the necessary images and audio files (e.g., background images, player image, bottle image, thorn image, and background music) in the assets folder.

Running the Game
To start the game, run the following command:

bash
Copy code
python game.py
The game will launch, and you can start playing.

How to Play
Move: Use the left and right arrow keys to move the player.
Goal: Collect the bottles that fall from the top of the screen. Each level has a bottle target to reach.
Avoid: Do not touch the thorns! Touching them will decrease your lives.
Levels: Collect a specific number of bottles in each level to progress. The falling speed of bottles and thorns will increase with each level.
Levels
Level 1: Collect 20 bottles.
Level 2: Collect 15 bottles (with faster falling items).
Level 3: Collect 10 bottles (with even faster falling items).
Game Over
The game ends when the player loses all lives or completes all levels.
Contributing
Feel free to fork the project and submit pull requests if you'd like to contribute. Any feedback or suggestions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Pygame community for providing the tools to create this game.
Background music and sound effects are sourced from free music resources.


