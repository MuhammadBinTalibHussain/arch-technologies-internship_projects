# Arch Technologies Internship — Python Mini Projects

A collection of beginner-to-intermediate Python projects built during my internship at **Arch Technologies**. This repository showcases GUI applications using **Tkinter** and a terminal-based AI game using the **Minimax algorithm with Alpha-Beta pruning**.

---

## Projects Included

| # | Project | Description | Tech Used |
|---|---------|-------------|-----------|
| 1 | **ATM Simulation** | A simple ATM interface to deposit, withdraw, and check balance | Tkinter, OOP |
| 2 | **Connect 4 (AI)** | Terminal-based Connect Four game against an AI opponent with adjustable difficulty | Minimax, Alpha-Beta Pruning |
| 3 | **Dice Rolling Game** | Rolls two dice and displays the total on click | Tkinter, Random |
| 4 | **Number Guessing Game** | Guess a randomly generated number between 1–100 with attempt tracking | Tkinter, Random |
| 5 | **To-Do List App** | Add and complete tasks with a live progress bar | Tkinter, ttk |

---

## 🖥️ Project Details

### 1. ATM Simulation (`ATMLogic.py`)

A simple banking simulation with an object-oriented backend (`ATM` class) and a Tkinter GUI (`ATMApp` class).

#### Features
- Deposit money
- Withdraw money (with insufficient balance check)
- Check current balance
- Starting balance: **5000**

#### Run

```bash
python ATMLogic.py
```

---

### 2. Connect 4 with AI (`Connect4.py`)

A fully playable Connect Four game in the terminal featuring a smart AI opponent powered by the **Minimax algorithm with Alpha-Beta pruning**.

#### Features
- Three difficulty levels:
  - Easy (Depth 3)
  - Medium (Depth 5)
  - Hard (Depth 7)
- Colored terminal board
- Horizontal, vertical, and diagonal win detection
- Score tracking across multiple rounds
- AI statistics:
  - Nodes searched
  - Evaluation score
  - Time taken

#### Run

```bash
python Connect4.py
```

---

### 3. Dice Rolling Game (`DiceRolling.py`)

A simple Tkinter application that simulates rolling two dice.

#### Features
- Rolls two random dice
- Displays both dice values
- Shows total score
- Clean and colorful interface

#### Run

```bash
python DiceRolling.py
```

---

### 4. Number Guessing Game (`NumberGuess.py`)

A classic number guessing game where the player must guess a randomly generated number between **1 and 100**.

#### Features
- Random number generation
- "Too High" and "Too Low" hints
- Attempt counter
- Input validation

#### Run

```bash
python NumberGuess.py
```

---

### 5. To-Do List App (`ToDoList.py`)

A simple task manager built with Tkinter.

#### Features
- Add new tasks
- Mark tasks as completed
- Live progress bar
- Warning messages for invalid actions

#### Run

```bash
python ToDoList.py
```

---

##  Requirements

- Python 3.x
- Tkinter (included with most Python installations)

No external libraries are required. All projects use Python's standard library.

---

##  Installation

```bash
git clone https://github.com/your-username/your-repository.git

cd your-repository

python <filename>.py
```

Replace `<filename>.py` with the project you want to run.

Example:

```bash
python Connect4.py
```

---

##  What I Learned

During my internship at **Arch Technologies**, I gained practical experience in:

- Building desktop GUI applications using Tkinter
- Applying Object-Oriented Programming (OOP)
- Developing AI game logic with Minimax and Alpha-Beta Pruning
- Handling user input validation and exceptions
- Organizing Python projects for readability and maintainability

---

##  Repository Structure

```
.
├── ATMLogic.py
├── Connect4.py
├── DiceRolling.py
├── NumberGuess.py
├── ToDoList.py
└── README.md
```

---

##  Author

**Muhammad Bin Talib Hussain**

Backend Developer | Machine Learning Enthusiast

Intern @ **Arch Technologies**

---

## License

This project is intended for educational and learning purposes.
