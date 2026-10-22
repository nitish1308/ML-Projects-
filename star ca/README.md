# ⭐ Star Catcher

**Star Catcher** is a 2D arcade game built with **Python** and **Pygame**. Move a bucket across a night sky to catch falling stars, avoid bombs, collect power-ups, and try to reach the highest score.

## Features

- Animated night-sky background with a moon, twinkling stars, drifting clouds, and mountains
- Smooth bucket movement with simple movement and catch animations
- Falling stars, collision detection, scoring, and lives
- Bomb obstacles that can cost you a life
- Power-ups, including:
  - **Magnet** — attracts falling stars
  - **Shield** — protects against a hit or a missed star while active
  - **Slow-Mo** — slows falling objects
  - **Double Points** — doubles the points earned from stars
  - **Extra Life** — restores a life
- Three difficulty levels: Easy, Medium, and Hard
- Four bucket skins: Wood, Gold, Ice, and Neon
- Level progression and bonus lives
- Start screen, player-name input, game-over screen, and retry option
- Persistent top-10 high scores stored locally in `highscores.json`
- Particle effects and screen shake for gameplay feedback

## Requirements

- Python 3.9 or later recommended
- Pygame

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed.
2. Open a terminal or command prompt in the project folder.
3. Install the dependency:

   ```bash
   python -m pip install pygame
   ```

## Run the Game

Run the main game file:

```bash
python star_catcher.py
```

If your system uses the `py` launcher on Windows, you can also try:

```bash
py star_catcher.py
```

## How to Play

1. Launch the game.
2. Enter a player name on the start screen (up to 12 characters).
3. Choose a bucket skin and difficulty.
4. Select **PLAY**.
5. Move the bucket to catch stars, avoid bombs, and collect power-ups.

### Controls

| Action | Control |
|---|---|
| Move left | `←` or `A` |
| Move right | `→` or `D` |
| Quit game | `Esc` or close the game window |
| Select menu options | Mouse click |
| Edit player name | Click the name field, then type; use `Backspace` to delete and `Enter` to finish |

### Gameplay Rules

- Catch falling stars to earn points.
- Missing a star costs a life unless the shield is active.
- Hitting a bomb costs a life unless the shield absorbs the hit.
- Collect power-ups to gain temporary advantages.
- The game ends when your lives reach zero.
- The level increases as your score rises. The game also awards bonus lives at score milestones, up to the configured life limit.

## Project Files

| File | Purpose |
|---|---|
| `star_catcher.py` | Main, complete game with menus, difficulty selection, skins, power-ups, levels, and high scores |
| `highscores.json` | Local JSON file used to save the top 10 scores |
| `class1_background.py` | Standalone learning version: animated night-sky background |
| `class2_player_bucket.py` | Adds the controllable bucket |
| `class3_falling_stars_and_score.py` | Adds falling stars, collisions, score, and lives |
| `class4_obstacles_powerups_shake.py` | Adds obstacles, power-ups, and screen shake |
| `class5_full_game_menus_and_highscores.py` | Learning version that combines the systems into a full game |

The `class1` through `class5` files are progressive standalone examples. To play the main game, use `star_catcher.py`.

## High Scores

Scores are saved in `highscores.json` in the same folder as the main game. The game keeps the 10 highest scores. If the file is missing or cannot be read, the game starts with an empty score list and can create the file when saving a score.

To reset the leaderboard, close the game and clear the contents of `highscores.json` to:

```json
[]
```

## Troubleshooting

- **`ModuleNotFoundError: No module named 'pygame'`**  
  Install Pygame with `python -m pip install pygame`.

- **The game does not launch with `python`**  
  Try `py star_catcher.py` on Windows, or confirm that Python is installed and available on your PATH.

- **High scores do not persist**  
  Make sure the game folder is writable and that `highscores.json` is alongside `star_catcher.py`.

## Built With

- **Python** — programming language
- **Pygame** — game window, rendering, input, collision detection, and game loop
- **JSON** — local high-score storage

## License

No license is specified in this project. Add a `LICENSE` file if you want to define how others may use, modify, and distribute the code.
