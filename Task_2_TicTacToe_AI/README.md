A Python-based Tic-Tac-Toe game where a human player competes against an AI agent.

The AI uses the Minimax algorithm to evaluate possible moves and choose the best move. This makes the AI extremely difficult to beat and demonstrates basic game theory and search algorithms.

Features
Human vs AI gameplay
Minimax-based AI
Win detection
Draw detection
Invalid move handling
Scoreboard
Replay option
Command-line interface
AI Algorithm
The AI uses the Minimax algorithm.

Minimax examines possible future game states and assigns scores:

+1 → AI wins
-1 → Human wins
0 → Draw
The AI selects the move with the highest possible score while assuming that the human player will always make the best possible move.

Project Structure
tic_tac_toe_ai/
│
├── main.py
├── game.py
├── board.py
├── ai.py
├── README.md
└── venv/
