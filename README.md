# Parta Ola Game (2025 Edition)

A Python implementation of the classic game **"Πάρτα Όλα"** (Take It All).  
Originally created in 2019, this is a modern, optimized version (2025) with a cleaner and more modular design.

---

## 📌 How the Game Works
- The game is played by **2 or more players**.
- Each player starts with the same number of beans (or tokens).
- At the start of each round, all active players put **1 bean into the pot**.
- Players take turns spinning the wheel, which can result in:
  - **Put One** → Player adds 1 bean to the pot.
  - **Put Two** → Player adds 2 beans to the pot (or as many as possible).
  - **Put All** → Every player adds 1 bean (if possible).
  - **Take One** → Player takes 1 bean from the pot.
  - **Take Two** → Player takes 2 beans (or as many as available).
  - **Take Them All** → Player takes all beans from the pot.
- If a player runs out of beans when required to put, they are **eliminated**.
- The game ends when **only one player remains**, or if all players are eliminated (tie).

---

## ✅ Features
- Random selection of the starting player.
- Dynamic number of players and starting beans.
- Automatic handling of eliminations and pot updates.
- Clean and modular Python code.
- Compatible with Python 3.8+.

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/parta-ola.git
   cd parta-ola
   ```
2. Run the game:
   ```bash
   python parta_ola.py
   ```

---

## 💡 Example Output
```
Number of players: 3
Number of beans per player: 2
The first player is Player 2

----------------------------------------
Round 1 begins: everyone puts 1
Pot: 3
Player 1 budget: 1
Player 2 budget: 1
Player 3 budget: 1

Player 2 spinned Take Them All
Pot: 0
Player 1 budget: 1
Player 2 budget: 4
Player 3 budget: 1
Pot is zero: round ends

Game finished: Player 2 wins
```

---

## 📂 Project Structure
```
├── parta_ola.py   # Main game file
├── README.md      # Project documentation
```

---

## 📜 License
This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project.

---

## 👩‍💻 Author
- Original Version (2019): **Maria Dimitropoulou**
- Modern Version (2025): **Refactored & Optimized**
